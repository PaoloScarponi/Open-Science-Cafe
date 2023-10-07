# external modules import
from pydantic import BaseModel


# class definition
class ProjectInfo(BaseModel):
    description: str
    keywords: list[str]
