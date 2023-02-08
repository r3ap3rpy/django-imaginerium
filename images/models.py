from django.db import models
from uuid import uuid4
# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 10)
    description = models.TextField(null = True, blank=True)
    image = models.ImageField(null = True, blank = True, default = 'default.jpg')
    created = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    id = models.UUIDField(default = uuid4, unique = True, editable = False, primary_key = True)
    def __str__(self):
        return self.name