from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class MyVideo(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()
    link = models.CharField(max_length=400,blank=True,null=True)

    def __str__(self):
        return str (self.title)

    class Meta:
        ordering = ['-added']
