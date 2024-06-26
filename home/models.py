from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    created = models.DateTimeField(null= True, blank=True)

    def __str__(self):
        return self.name