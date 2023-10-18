from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=150)
    price=models.DecimalField(decimal_places=2,max_digits=8)
    imageurl=models.CharField(max_length=2083,blank=True,default=False)
    bookavailable=models.BooleanField(default=False)
    description=models.CharField(max_length=600,default='')


class Cart(models.Model):
    objects = None
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Books)
    total_price = models.DecimalField(max_digits=10,decimal_places=5)

class CartItems(models.Model):
    book= models.ForeignKey(Books,on_delete=models.CASCADE)
    cart= models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return f'{self.quantity} * {self.book}'
    #
    # def total_price(self):
    #     return self.books.price * self.quantity