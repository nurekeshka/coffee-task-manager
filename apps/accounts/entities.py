''' This file contains entities of accounts application. '''
from datetime import datetime

from apps.common.entities import AbstractEntity


class User(AbstractEntity):
    ''' This class repressents a user entity. '''

    def __init__(self):
        self.__identity: int = None
        self.__username: str = None
        self.__first_name: str = None
        self.__last_name: str = None
        self.__email: str = None
        self.__is_staff: bool = None
        self.__is_active: bool = None
        self.__date_joined: datetime = None

    @classmethod
    def set_params(cls, **params) -> 'User':
        ''' Set the parameters of the user object. '''
        cls.__identity: int = params.pop('identity')
        cls.__username: str = params.pop('username')
        cls.__first_name: str = params.pop('first_name')
        cls.__last_name: str = params.pop('last_name')
        cls.__email: str = params.pop('email')
        cls.__is_staff: bool = params.pop('is_staff')
        cls.__is_active: bool = params.pop('is_active')
        cls.__date_joined: datetime = params.pop('date_joined')

    @property
    def identity(self) -> int:
        ''' This is the ID of the user '''
        return self.__identity

    @property
    def username(self) -> str:
        ''' This is the username of the user '''
        return self.__username

    @property
    def first_name(self) -> str:
        ''' This is the first name of the user '''
        return self.__first_name

    @property
    def last_name(self) -> str:
        ''' This is the last name of the user '''
        return self.__last_name

    @property
    def email(self) -> str:
        ''' This is the email address of the user '''
        return self.__email

    @property
    def is_staff(self) -> bool:
        ''' This shows if the user is a staff member '''
        return self.__is_staff

    @property
    def is_active(self) -> bool:
        ''' This shows if the user is active '''
        return self.__is_active

    @property
    def date_joined(self) -> datetime:
        ''' This shows when the user was created '''
        return self.__date_joined
