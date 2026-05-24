from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseTool(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass
        
    @property
    @abstractmethod
    def schema(self) -> Dict[str, Any]:
        """Returns JSON schema for the tool arguments."""
        pass

    @abstractmethod
    async def execute(self, **kwargs) -> str:
        """Executes the tool with given arguments and returns the result as string."""
        pass
