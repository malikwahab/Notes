from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=140)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='notes')

    def __str__(self):
        return self.title
