from dataclasses import dataclass
from enum import Enum
from discord import Message

class Privacy(Enum):
    PUBLIC = 0
    HIDDEN = 1

@dataclass
class Action:
    msg: Message = None
    privacy: Privacy = Privacy.PUBLIC
    statement: str = None