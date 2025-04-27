from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
            ('drink','Drink'),
            ('food','Food'),
            ('fruit','Fruit'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length = 10, choices= CATEGORY_CHOICES)
    description = models.TextField( blank=True)
    price = models.DecimalField(max_digits= 6, decimal_places= 2)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"