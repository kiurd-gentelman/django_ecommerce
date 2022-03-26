from django.db import models


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brand/')
    description = models.TextField()
    foundation_date = models.DateField()

    def __str__(self):
        return self.name
