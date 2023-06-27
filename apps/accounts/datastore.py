''' This file contains Database repositories of the application. '''
from typing import List

from apps.common.exceptions import EntityDoesNotExist
from apps.accounts.models import User as UserORM
from apps.accounts.entities import User


class UserDBRepository:
    ''' This class represents user datastore repositories. '''

    @classmethod
    def get_find_by_id(cls, identity: int) -> List[User]:
        ''' Find a user by id from the database and return entity. '''
        try:
            orm_user = UserORM.objects.get(id=identity)
        except UserORM.DoesNotExist as exception:
            raise EntityDoesNotExist from exception

        return cls.decode_orm_user(orm_user)

    @classmethod
    def get_find(cls) -> List[User]:
        ''' Get all users from the database and return as entities. '''
        try:
            orm_users = UserORM.objects.all()
        except UserORM.DoesNotExist as exception:
            raise EntityDoesNotExist from exception

        return cls.decode_orm_users(orm_users)

    @classmethod
    def decode_orm_user(cls, orm_user_queryset: UserORM) -> List[User]:
        ''' Decode an ORM user into a user entity. '''
        user = User()

        user_entity = user.set_params(
            identity=orm_user_queryset.pk,
            username=orm_user_queryset.username,
            first_name=orm_user_queryset.first_name,
            last_name=orm_user_queryset.last_name,
            email=orm_user_queryset.email,
            is_staff=orm_user_queryset.is_staff,
            is_active=orm_user_queryset.is_active,
            date_joined=str(
                orm_user_queryset.date_joined.strftime('%Y/%m/%d')),
        )

        return [user_entity]

    @classmethod
    def decode_orm_users(cls, orm_user_queryset: List[UserORM]) -> List[User]:
        ''' Decode multiple users into user entities. '''
        return [cls.decode_orm_user(orm_user)[0]
                for orm_user in orm_user_queryset]
