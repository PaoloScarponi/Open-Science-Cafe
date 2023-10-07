# external modules import
from enum import Enum

# enumerate definition
class UserRole(str, Enum):
    SURFER = "Surfer"
    CONTRIBUTOR = "Contributor"
    CREATOR = "Creator"
