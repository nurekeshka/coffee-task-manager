''' This file contains entities of tasks application '''
from datetime import datetime


class Task:
    ''' This class represents a task's entity '''

    def __init__(self):
        self.__identity: int = None

        self.__name: str = None
        self.__description: str = None

        self.__assignee: int = None
        self.__status: int = None
        self.__organization: int = None

        self.__startdate: datetime = None
        self.__deadline: datetime = None

    @classmethod
    def set_params(cls, **kwargs) -> 'Task':
        ''' Set the parameters of the task object '''
        cls.__identity: int = kwargs.pop('identity')
        cls.__name: str = kwargs.pop('name')
        cls.__description: str = kwargs.pop('description')
        cls.__assignee: int = kwargs.pop('assignee')
        cls.__status: int = kwargs.pop('status')
        cls.__organization: int = kwargs.pop('organization')
        cls.__startdate: datetime = kwargs.pop('startdate')
        cls.__deadline: datetime = kwargs.pop('deadline')

        return cls

    @property
    def identity(self) -> int:
        ''' This is the identity of the task '''
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
    def startdate(self) -> datetime:
        ''' This is the start date of the task '''
        return self.__startdate

    @property
    def deadline(self) -> datetime:
        ''' This is the deadline of the task '''
        return self.__deadline
