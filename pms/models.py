from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

class SaveData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=120)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=25, null=True, blank=True)

    def save(self, *args, **kwargs):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(-_=+)'
        self.password = get_random_string(length=16, allowed_chars=chars)
        super(SaveData, self).save(*args, **kwargs)

        