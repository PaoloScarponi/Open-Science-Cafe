# external modules import
from enum import Enum

# enumerate definition
class ProjectStatus(str, Enum):
    NOT_STARTED = "Not-Started"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    EXPIRED = "Expired"