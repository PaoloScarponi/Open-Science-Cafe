# external modules import
from enum import Enum

# enumerate definition
class CommType(str, Enum):
    TEXT = "Text"
    MAIL = "E-Mail"
    PHONE = "Phone"
