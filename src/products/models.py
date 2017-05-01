from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField("Category", blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d',
                                null=True, blank=True)

    def __str__(self):
        return self.title


class Valiation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120)
    price = models.IntegerField(null=False, blank=False)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default="-1", null=True, blank=True) # -1 == no limit

    def __str__(self):
        return self.title

    def get_price(self):
        if sale_price:
            return self.sale_price
        else:
            return self.price

class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
