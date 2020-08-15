from django.db import models

# Create your models here.


class LinkEntry(models.Model):
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.text + " " + self.link + " " + self.image

