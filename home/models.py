from django.db import models

# Create your models here.

class Contacts(models.Model):

    SNo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)
    content = models.TextField()


    def __str__(self):
        return f"This is the form {self.name} - {self.email}"
