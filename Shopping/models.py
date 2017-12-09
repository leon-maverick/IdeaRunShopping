from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):

    title = models.CharField(max_length=50, verbose_name=_('title of related category'))
    sold_price = models.IntegerField(default=0 , verbose_name=_('sold price'))
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    price = models.IntegerField(verbose_name=_('price'))
    sold_price = models.IntegerField(default=0, verbose_name=_('sold price'))

    description = models.TextField(verbose_name=_('description'))
    # todo why not ImageField?
    # todo not "picture"? it's not like we're charged by characters used :D
    # using full words increases code readability
    pic = models.FileField(blank=True, verbose_name=_('picture'))
    # //todo we should always define the "related_name" for relational fields (fk, m2m).
    cat = models.ForeignKey(Category, related_name='category', verbose_name=_('Category'))
    available = models.IntegerField(verbose_name=_('Available'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title + " " + self.cat.title

    def cat_title(self):
        return self.cat.title


class NotAvProManager(models.Manager):
    def get_queryset(self):
        return super(NotAvProManager, self).get_queryset().filter(available=0)


class NotAvPro(Product):
    objects = NotAvProManager()
    class Meta:
        verbose_name = _('Not available product')
        verbose_name_plural=_('Not available products')
        proxy = True

    def __str__(self):
        return self.title


class Order(models.Model):

    STAT = (("P", "Pending"),
            ("D", "Done"),
            ("C", "Cancel"),
            ("H", "Handeling"))

    person = models.ForeignKey('auth.User', related_name='orders', verbose_name=_('Ordered person') )
    date = models.DateField(auto_now_add=True, verbose_name=_('Date'))
    products = models.ManyToManyField(Product, verbose_name=_('orders products'))  # TODO a reD MANY TO MANAY DOC ANF ITS TABLE
    status = models.CharField(max_length=1, choices=STAT, default='P',verbose_name=_('Order status'))
    total_price = models.IntegerField(default=0, verbose_name=_('Order Price'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.status == "D" and self.__original_status == "P":
            for p in (self.products.all()):
                p.available = p.available - 1
                p.sold_price = p.sold_price + p.price
                p.cat.sold_price = p.cat.sold_price + p.price
                cat = p.cat
                print(p.cat.title)
                cat.save()
                p.save()

        elif self.status == "C" and self.__original_status == "D":
            for p in (self.products.all()):
                p.available = p.available + 1
                p.sold_price = p.sold_price - p.price
                p.cat.sold_price = p.cat.sold_price - p.price
                cat = p.cat
                print(p.cat.title)
                cat.save()
                p.save()

        return super().save(force_insert=force_insert, force_update=force_update, *args, **kwargs)





