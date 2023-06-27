''' This file contains tests for the accounts application. '''
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from apps.accounts.models import User, Organization


class UserAPITestCase(APITestCase):
    username = 'admin'
    password = 'root'

    email = 'admin@example.com'

    first_name = 'John'
    last_name = 'Doe'

    def test__creation(self):
        link = reverse('users')

        response = self.client.post(link, {
            'username': self.username,
            'password': self.password,
        })

        token = Token.objects.get(user__username=self.username)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['authentication-token'], token.key)
