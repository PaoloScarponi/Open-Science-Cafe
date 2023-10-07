# external modules import
from enum import Enum

# enumerate definition
class UserStatus(str, Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    VERIFIED = "Verified"
