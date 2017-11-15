from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category (models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product (models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    pic = models.FileField(blank=True)
    cat= models.ForeignKey(Category)
    available = models.IntegerField()

    def __str__(self):
        return self.title + " " + self.cat.title

class Order (models.Model):
    STAT = (("P", "Pending"),
            ("D", "Done"),
            ("C", "Cancel"),
            ("H", "Handeling"))

    person = models.ForeignKey('auth.User', related_name='orders',)
    date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product) #TODO a reD MANY TO MANAY DOC ANF ITS TABLE
    status = models.CharField(max_length=1, choices=STAT,default='P')
    #sum = get_sum()

    def __str__(self):
        return str(self.person.username) +" " +self.status

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.status=="D" and self.__original_status=="P" :
            print("It is Done")
            for p in (self.products.all()):
                p.available = p.available - 1
                p.save()

        elif self.status=="C" and self.__original_status=="D" :
            print("Canceled")
            for p in (self.products.all()):
                p.available = p.available + 1
                p.save()

        return super().save(force_insert=force_insert,force_update=force_update,*args,**kwargs)

    def get_sum(self):

        sum = 0
        for items in self.products.all():
            sum = sum + items.price
        return sum