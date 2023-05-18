from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def discounted_price(self):
        if hasattr(self, 'promotion'):
            discount = Decimal(self.promotion.discount_percentage / 100)
            return round(self.price * (1 - discount), 2)
        else:
            return self.price


class Promotion(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def is_active(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    def __str__(self):
        return f"{self.product.name} - {self.discount_percentage}%"
