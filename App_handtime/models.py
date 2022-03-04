from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.email


class User(models.Model):
    usertype = models.CharField(max_length=100, default="customer")
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email + " - " + self.usertype


class AddProduct(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    productname = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    file = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.productname + " - " + str(self.seller)


class Wishlists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.email


class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    qty = models.IntegerField(default=1)
    totalprice = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions',
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(
        unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime(
                'PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
