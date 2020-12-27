from django.db import models
# See also project/settings.py MYAUTH_PASSWORD_VALIDATORS
class MyUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
