from typing import Optional, Any
from pydantic import BaseModel


class Problem(BaseModel):
    """
    Problem model
    
    Args:
        BaseModel: BaseModel

    Returns:
        Problem: Problem model
    """
    title: str
    status: int
    detail: Any
    type: Optional[str] = None
    instance: Optional[str] = None

    def dict(self, *args, **kwargs):
        """
        dict method
        
        Returns:
            dict: dict
        """
        kwargs.pop("exclude_unset")
        return super().dict(*args, exclude_unset=True, **kwargs)
