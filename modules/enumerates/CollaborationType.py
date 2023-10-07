# external modules import
from enum import Enum

# enumerate definition
class CollaborationType(str, Enum):
    ONSITE = "On-Site"
    HYBRID = "Hybrid"
    REMOTE = "Remote"
