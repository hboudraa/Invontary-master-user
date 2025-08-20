from django.db import models


# Create your models here.
class Supplier(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=False)
    raison_social = models.CharField(max_length=100, null=True, blank=False)
    agisant = models.CharField(max_length=100, null=True, blank=False)
    address = models.CharField(max_length=100, null=True, blank=False)
    phone = models.CharField(max_length=100, null=True, blank=False)
    phone_2 = models.CharField(max_length=100, null=True, blank=False)
    email = models.CharField(max_length=100, null=True, blank=False)
    fax = models.CharField(max_length=100, null=True, blank=False)
    nin = models.CharField(max_length=100, null=True, blank=False)
    rip = models.CharField(max_length=100, null=True, blank=False)
    agence = models.CharField(max_length=100, null=True, blank=False)
    num_rc = models.CharField(max_length=100, null=True, blank=False)
    num_agriment = models.CharField(max_length=100, null=True, blank=False)
    nif = models.CharField(max_length=100, null=True, blank=False)
    nis = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return f"{self.full_name}" + " - " + f"{self.phone}"