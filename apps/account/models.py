from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Table for internal info about users
    """

    referrer = models.URLField(verify_exists=False, blank=True, max_length=255)
    user = models.OneToOneField('auth.User')


class Profile(models.Model):
    
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    
    gender = models.Choices
    image = models.ImageField(upload_to="profile_picture", blank=True)

    city = models.CharField(max_length=100, blank=True)



