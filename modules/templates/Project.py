# external modules import
from pydantic import BaseModel

# internal modules import
from ..enumerates import CollaborationType, ProjectStatus

# class definition
class Project(BaseModel):
    title: str
    description: str
    start_date: str
    end_date: str
    owners: list[str]
    collaborators: list[str]
    keywords: list[str]
    country: str
    languages: list[str]
    collaboration_type: CollaborationType
    status: ProjectStatus
    official_website: str = None
    project_repository: str = None