from app.core.config import settings
from app.providers.openai_compatible import OpenAICompatibleProvider
from typing import Optional

class ProviderRegistry:
    @staticmethod
    def get_provider(provider_name: str) -> Optional[OpenAICompatibleProvider]:
        if provider_name == "local":
            return OpenAICompatibleProvider(
                base_url=settings.LOCAL_PROVIDER_URL,
                api_key="not-needed"
            )
        elif provider_name == "google":
            # Google AI Studio OpenAI compatible endpoint
            if not settings.GOOGLE_API_KEY:
                raise ValueError("GOOGLE_API_KEY is not set.")
            return OpenAICompatibleProvider(
                base_url="https://generativelanguage.googleapis.com/v1beta/openai",
                api_key=settings.GOOGLE_API_KEY
            )
        elif provider_name == "openai":
            if not settings.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY is not set.")
            return OpenAICompatibleProvider(
                base_url="https://api.openai.com/v1",
                api_key=settings.OPENAI_API_KEY
            )
        else:
            raise ValueError(f"Unknown provider: {provider_name}")
