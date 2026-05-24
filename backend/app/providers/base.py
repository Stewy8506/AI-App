from abc import ABC, abstractmethod
from typing import AsyncGenerator, List, Dict, Any

class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.
    """
    
    @abstractmethod
    async def generate(self, messages: List[Dict[str, Any]], model: str, **kwargs) -> str:
        """Generate a complete response."""
        pass
        
    @abstractmethod
    async def stream(self, messages: List[Dict[str, Any]], model: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream the response back as an async generator."""
        pass

    @abstractmethod
    async def get_models(self) -> List[str]:
        """Fetch available models for the provider."""
        pass

