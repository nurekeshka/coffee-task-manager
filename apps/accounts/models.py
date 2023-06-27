''' This file contains account models
    related to authentication processes
'''
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db import models

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Organization(models.Model):
    ''' This model represents organization in database. '''
    name: str = models.CharField(max_length=255, verbose_name='name')
    creator: User = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True,
        null=True, verbose_name='creator')

    class Meta:
        ''' Meta data for organization models. '''
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self) -> str:
        return str(self.name)


@receiver(models.signals.post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
