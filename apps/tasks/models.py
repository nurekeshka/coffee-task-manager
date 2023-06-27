''' This file contains the models of tasks application
    Usually they are defined as ModelORM objects
'''
from datetime import datetime

from django.db import models

from apps.accounts.models import Organization, User
from apps.tasks.constants import TaskStatus


class Task(models.Model):
    ''' This model represents tasks in database. '''
    name: str = models.CharField(max_length=255, verbose_name='name')
    description: str = models.TextField(verbose_name='descriptions')

    assignee: User = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name='assignee')

    organization: Organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, blank=False, null=False,
        verbose_name='organization')

    status: int = models.SmallIntegerField(
        choices=TaskStatus.get_choices(), default=TaskStatus.PLANNED.value,
        verbose_name='status')

    startdate: datetime = models.DateTimeField(
        verbose_name='start date',  blank=True, null=True)

    deadline: datetime = models.DateTimeField(
        verbose_name='deadline', blank=True, null=True)

    class Meta:
        ''' Meta data for the task model. '''
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self) -> str:
        return str(self.name)
