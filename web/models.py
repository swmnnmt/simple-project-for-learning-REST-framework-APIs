from django.db import models
from django.utils.timezone import now


# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=150)
    story_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default='', upload_to='web/story_image/', blank = True, null = True)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.story_name
