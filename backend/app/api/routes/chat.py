from fastapi import APIRouter, HTTPException, Request
from sse_starlette.sse import EventSourceResponse
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from app.providers.registry import ProviderRegistry

router = APIRouter()

class ChatRequest(BaseModel):
    provider: str
    model: str
    messages: List[Dict[str, Any]]
    temperature: Optional[float] = 0.7

@router.post("/completions")
async def chat_completions(request: ChatRequest, req: Request):
    try:
        provider_instance = ProviderRegistry.get_provider(request.provider)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    if not provider_instance:
        raise HTTPException(status_code=400, detail="Provider not found")
        
    async def event_generator():
        try:
            async for chunk in provider_instance.stream(
                messages=request.messages,
                model=request.model,
                temperature=request.temperature
            ):
                if await req.is_disconnected():
                    break
                yield {
                    "event": "message",
                    "data": chunk
                }
            yield {
                "event": "done",
                "data": "[DONE]"
            }
        except Exception as e:
            yield {
                "event": "error",
                "data": str(e)
            }

    return EventSourceResponse(event_generator())
