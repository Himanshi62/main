from django.db import models

# Create your models here.
class Notify(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    colg = models.CharField(max_length = 200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return (
            f"{self.name}"
        )