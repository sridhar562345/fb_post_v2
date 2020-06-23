import enum

from ib_common.constants import BaseEnumClass

class ReactionType(BaseEnumClass, enum.Enum):
    LIKE = "LIKE"
    WOW = "WOW"
    HAHA = "HAHA"
    DISLIKE = "DISLIKE"
    SAD = "SAD"
    ANGRY = "ANGRY"
