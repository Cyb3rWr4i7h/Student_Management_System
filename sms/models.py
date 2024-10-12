from django.db import models

# Create your models here.

class Help(models.Model):
    userID = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    problem = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.userID
    