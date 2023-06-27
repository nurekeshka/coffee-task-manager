''' This file contains tests for the accounts application. '''
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from apps.accounts import datastore
from apps.accounts import entities
from apps.accounts import models


class UserAPITestCase(APITestCase):
    username = 'admin'
    password = 'root'

    email = 'admin@example.com'

    first_name = 'John'
    last_name = 'Doe'

    def test__datastore_decodes_user(self):
        user_orm = models.User.objects.create(
            username=self.username, email=self.email,
            first_name=self.first_name, last_name=self.last_name)
        user_entity = datastore.UserDBRepository.get_find_by_id(user_orm.pk)[0]

        self.assertEqual(user_orm.pk, user_entity.identity)

    def test__datastore_decodes_users(self):
        user_orm = models.User.objects.create(
            username=self.username, email=self.email,
            first_name=self.first_name, last_name=self.last_name)

        user_entity = datastore.UserDBRepository.get_find()[0]

        self.assertEqual(len(user_entity), 1)
        self.assertEqual(user_entity.email, user_orm.email)
