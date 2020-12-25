from django.db import models

from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    def __str__(self):
        return self.note

