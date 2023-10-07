# external modules import
from pydantic import BaseModel


# class definition
class UserSkills(BaseModel):
    skills: list[str]