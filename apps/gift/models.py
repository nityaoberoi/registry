from django.contrib.auth.models import User
from django.db import models

def set_image_filename(instance, filename):
    """
    Returns filename based on slug
    """
    return "image/{}".format(filename)

class GiftList(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    private = models.BooleanField(default=False)
    event_date = models.DateTimeField(null=True)
    
    users = models.ManyToManyField('auth.User')

class Item(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=set_image_filename, max_length=200, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    requested_qty = models.PositiveSmallIntegerField(default=0)
    
    price_fulfilled = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True)

    lists = models.ManyToManyField('list.GiftList')
