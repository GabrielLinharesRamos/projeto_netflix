from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=5000)
    url=models.CharField(max_length=500)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title