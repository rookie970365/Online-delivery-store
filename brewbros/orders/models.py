from django.db import models
from products.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    # order_key = models.CharField(max_length=200)
    # coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True)
    # discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.pk}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.pk}'

    def get_cost(self):
        return self.price * self.quantity
