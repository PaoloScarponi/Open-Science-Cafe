# external modules import
from enum import Enum

# enumerate definition
class CollaborationState(str, Enum):
    PENDING = "Pending"
    ONGOING = "Ongoing"
    TERMINATED = "Terminated"
