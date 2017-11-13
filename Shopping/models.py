from django.db import models
from django.contrib.auth.models import User

class Category (models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product (models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    pic = models.FileField()
    cat= models.ForeignKey(Category)
    available = models.IntegerField()

    def __str__(self):
        return self.title + " " + self.cat.title

class Order (models.Model):
    STAT = (("P", "Pending"), ("D", "Done"), ("C", "Cancel"), ("H", "Handeling"))
    person = models.ForeignKey(User)
    date = models.DateField()
    products = models.ManyToManyField(Product)
    status = models.CharField(max_length=1, choices=STAT)
    #sum = get_sum()

    def get_sum(self):
        sum = 0
        for items in self.products:
            sum = sum + items.price
        return sum