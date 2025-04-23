from django.core.validators import RegexValidator
from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    user = models.ForeignKey(
        User, related_name="products", on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=100)
    description = tinymce_models.HTMLField(blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)

    @property
    def total(self):
        return self.price * self.quantity


class FicheStockEntr(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    name_fiche = models.ForeignKey(Product, on_delete=models.CASCADE)  # 🔹 إضافة علاقة بالمنتج
    date = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=10)
    source = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    observation = tinymce_models.HTMLField(blank=True, null=True)
    def __str__(self):
        return f"{self.date} | {self.name_fiche} | {self.source}"


# 🔹 إضافة إشارة لتحديث كمية المنتج عند إدخال مخزون جديد
@receiver(post_save, sender=FicheStockEntr)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:  # 🔹 فقط عند إنشاء سجل جديد
        product = instance.name_fiche  # المنتج المرتبط بالسجل
        product.quantity += instance.quantity  # 🔹 إضافة الكمية الجديدة
        product.save()  # 🔹 حفظ التحديثات


class FicheStockSortie(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    name_fiche = models.ForeignKey(Product, on_delete=models.CASCADE)  # 🔹 إضافة علاقة بالمنتج
    date = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=20)
    destination = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)
    observation = tinymce_models.HTMLField(blank=True, null=True)
    def __str__(self):
        return f"{self.date} | {self.name_fiche} | {self.destination}"

# 🔹 إضافة إشارة لتحديث كمية المنتج عند إخراج مخزون جديد
@receiver(post_save,sender=FicheStockSortie)
def update_product_quantity_sortie(sender, instance, created, **kwargs):
    if created:
        product = instance.name_fiche  # المنتج المرتبط بالسجل
        product.quantity -= instance.quantity  # 🔹 إضافة الكمية الجديدة
        product.save()  # 🔹 حفظ التحديثات


class DemandClass(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('rejected', 'Rejetée'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_demand = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Demande de {self.user} pour {self.name_demand}"

