from django.db import models

# Create your models here.
class Supplier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}" + " - " + f"{self.last_name}"