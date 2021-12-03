from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    items = models.CharField(max_length=1000)

    def __str__(self):
        return self.items

    date_created = models.DateTimeField(default=datetime.now, blank=True)

    

