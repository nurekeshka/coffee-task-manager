''' This file contains constants for tasks application '''
from typing import Tuple
import enum


class TaskStatus(enum.IntEnum):
    ''' Task status enum class '''
    REMOVED = 0
    PLANNED = 1
    IN_PROGRESS = 2
    DONE = 3

    @classmethod
    def get_choices(cls) -> Tuple[int]:
        ''' Get the list of status choices '''
        return tuple((choice.value, choice.name) for choice in cls)
