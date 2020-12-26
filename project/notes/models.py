from django.db import models

from django.contrib.auth.models import User

class Note(models.Model):
    owner_name = models.TextField()
    note = models.TextField()
    
    def __str__(self):
        return self.note

    class Meta:
        db_table = "note"
