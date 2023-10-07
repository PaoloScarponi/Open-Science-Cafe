# external modules import
from pydantic import BaseModel

# internal modules import
from ..enumerates import CollaborationState

# class definition
class ContributedProject(BaseModel):
    project_name: str
    collaboration_state: CollaborationState
