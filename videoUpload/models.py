from django.db import models

# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length=50)
    video = models.FileField(upload_to="video/%y")
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.caption