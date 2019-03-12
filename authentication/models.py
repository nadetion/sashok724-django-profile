from django.db import models
from django.contrib.auth.models import User
import os


def skin_upload_to(instance, filename):
    return os.path.join('mc/skins/' + instance.user.username + '.png')

def skin_upload_to(instance, filename):
    return os.path.join('mc/cloaks/' + instance.user.username + '.png')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skin = models.ImageField(upload_to=skin_upload_to)
    cloak = models.ImageField(upload_to=skin_upload_to)
