from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.


class Commune(models.Model):
    num_commune = models.CharField(max_length=4)
    name_commune = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.num_commune}" + "    " + f"{self.name_commune}"


# المندوبية الولائية
class Utilisateur(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT)
    name_french = models.CharField(max_length=80)
    name_arabic = models.CharField(max_length=80, default='غير معروف')
    date_of_birth = models.DateField()
    nin = models.CharField(max_length=18, null=False, blank=False)
    rip = models.CharField(max_length=20, default="00799999")
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message=_("Phone number must be 10 digits.")
    )
    fax_validator = RegexValidator(
        regex=r'^\d{9}$',
        message=_("Fax number must be 9 digits.")
    )
    phone = models.CharField(max_length=10, validators=[phone_validator], default='0900000000')
    phone_2 = models.CharField(max_length=10, validators=[phone_validator], blank=True, null=True)
    fax = models.CharField(max_length=9, validators=[fax_validator], default='034000000')
    email = models.EmailField(max_length=50, default='gmail@gmail.com')  # EmailField for validation
    recruitment = models.DateTimeField()
    def __str__(self):
        return f"{self.name_french} | {self.phone}"


class Charger(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='chargers')
    name_french = models.CharField(max_length=50)
    name_arabic = models.CharField(max_length=50)
    date_birth = models.DateField()
    commune_birth = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='commune_birth_charger')
    nin = models.CharField(max_length=18, null=False, blank=False)
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message=_("Phone number must be 10 digits.")
    )
    fax_validator = RegexValidator(
        regex=r'^\d{9}$',
        message=_("Fax number must be 9 digits.")
    )
    phone = models.CharField(max_length=10, validators=[phone_validator], default='0900000000')
    phone_2 = models.CharField(max_length=10, validators=[phone_validator], blank=True, null=True)
    rip = models.CharField(max_length=20, default="00799999")
    grade = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default='gmail@gmail.com')  # EmailField for validation
    observation = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.name_french} | {self.phone}"


class Delegue(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='delegues')
    name_french = models.CharField(max_length=50)
    name_arabic = models.CharField(max_length=50)
    date_birth = models.DateField()
    commune_birth = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='delegues_birth')
    nin = models.CharField(max_length=18, null=False, blank=False)
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message=_("Phone number must be 10 digits.")
    )
    fax_validator = RegexValidator(
        regex=r'^\d{9}$',
        message=_("Fax number must be 9 digits.")
    )
    phone = models.CharField(max_length=10, validators=[phone_validator], default='0900000000')
    phone_2 = models.CharField(max_length=10, validators=[phone_validator], blank=True, null=True)
    rip = models.CharField(max_length=20, default="00799999")
    grade = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default='gmail@gmail.com')  # EmailField for validation
    observation = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.name_french} | {self.phone}"


class SG(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT)
    name_french = models.CharField(max_length=50)
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message=_("Phone number must be 10 digits.")
    )
    fax_validator = RegexValidator(
        regex=r'^\d{9}$',
        message=_("Fax number must be 9 digits.")
    )
    phone = models.CharField(max_length=10, validators=[phone_validator], default='0900000000')
    phone_2 = models.CharField(max_length=10, validators=[phone_validator], blank=True, null=True)
    fax = models.CharField(max_length=9, validators=[fax_validator], default='034000000', blank=True, null=True)
    fix = models.CharField(max_length=9, validators=[fax_validator], default='034000000', blank=True, null=True)
    def __str__(self):
        return f"{self.name_french} | {self.phone}"


class Requisition(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='requisitions')
    name_french = models.CharField(max_length=50)
    name_arabic = models.CharField(max_length=50)
    date_birth = models.DateField()
    commune_birth = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='requisitions_birth')
    nin = models.CharField(max_length=18, null=False, blank=False)
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message=_("Phone number must be 10 digits.")
    )
    fax_validator = RegexValidator(
        regex=r'^\d{9}$',
        message=_("Fax number must be 9 digits.")
    )
    phone = models.CharField(max_length=10, validators=[phone_validator], default='0900000000')
    phone_2 = models.CharField(max_length=10, validators=[phone_validator], blank=True, null=True)
    rip = models.CharField(max_length=20, default="00799999")
    grade = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default='gmail@gmail.com')  # EmailField for validation
    created_at = models.DateTimeField(auto_now_add=True)
    observation = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.name_french} | {self.phone}"
