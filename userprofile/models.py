from django.contrib.auth.models import User
from django.db import models


class Userprofile(models.Model):
    user = models.ForeignKey(User, related_name='Userprofile', on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

def __str__(self):
    return self.user.username