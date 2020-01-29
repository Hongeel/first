# -*- encoding: utf-8 -*-
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse



# Create your models here.

def image_file_path(instance, filename):
    user = instance.user.username
    return f"{user}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to=image_file_path, blank=True)

    def __str__(self):
        username = self.user.username
        return f"{self.__class__.__name__}: {username}"

    def get_absolute_url(self):
        profile_user = self.user.id
        return reverse('profile')