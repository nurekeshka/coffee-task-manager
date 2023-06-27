''' This file contains entities of tasks application '''
from datetime import datetime
import dataclasses

from apps.common.entities import AbstractEntity


class Task(AbstractEntity):
    ''' This class represents a task's entity '''

    @dataclasses.dataclass
    class Dates:
        ''' Task dates dataclass '''
        startdate: datetime
        deadline: datetime

    def __init__(self):
        self.__identity: int = None

        self.__name: str = None
        self.__description: str = None

        self.__assignee: int = None
        self.__status: int = None
        self.__organization: int = None

        self.__calendar = self.Dates(startdate=None, deadline=None)

    @classmethod
    def set_params(cls, **params) -> 'Task':
        ''' Set the parameters of the task object '''
        cls.__identity: int = params.pop('identity')
        cls.__name: str = params.pop('name')
        cls.__description: str = params.pop('description')
        cls.__assignee: int = params.pop('assignee')
        cls.__status: int = params.pop('status')
        cls.__organization: int = params.pop('organization')
        cls.__calendar: cls.Dates = cls.Dates(startdate=params.pop(
            'startdate'), deadline=params.pop('deadline'))

        return cls

    @property
    def identity(self) -> int:
        ''' This is the ID of the task '''
        return self.__identity

    @property
    def name(self) -> str:
        ''' This is the name of the task '''
        return self.__name

    @property
    def description(self) -> str:
        ''' This is the description of the task '''
        return self.__description

    @property
    def assignee(self) -> int:
        ''' This is the assignee of the task '''
        return self.__assignee

    @property
    def status(self) -> int:
        ''' This is the status of the task '''
        return self.__status

    @property
    def organization(self) -> int:
        ''' This is the organization of the task '''
        return self.__organization

    @property
    def calendar(self) -> datetime:
        ''' This is the start date of the task '''
        return self.__calendar
