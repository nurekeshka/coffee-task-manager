# ''' This file contains tests for the tasks application '''
# from typing import Dict

# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse

# from apps.tasks.models import User, Organization


# class TaskAPITestCase(APITestCase):
#     ''' Tasks API tests case '''
#     user: User = User.objects.create(username='Chief Executive Officer')
#     organization: Organization = Organization.objects.create(
#         name='Coffee Inc.')

#     link = reverse('tasks')
#     data: Dict[str, str | int] = {
#         'name': 'Development of tasks module',
#         'description': 'During this process you should create tasks module.',
#         'organization': organization.pk,
#         'start_date': '2011-01-13',
#         'deadline': '2023-01-13',
#     }

#     def test_create_task(self):
#         ''' Testing task creation process '''
#         response = self.client.post(self.link, self.data, )

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
