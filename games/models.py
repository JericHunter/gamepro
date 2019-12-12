from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    release_date = models.DateTimeField('date released', blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.name
