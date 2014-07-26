from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Condition(models.Model):
    condition = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{}".format(self.condition)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{}".format(self.name)


class Item(models.Model):
    item = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="item_category")
    post_user = models.ForeignKey(User, related_name='user_post')
    description = models.TextField(max_length=4000)
    price = models.PositiveSmallIntegerField()
    deposit = models.PositiveSmallIntegerField()
    condition = models.ForeignKey(Condition, related_name="item_condition")
    beg_availability = models.DateTimeField(null=False)
    end_availability = models.DateTimeField(null=False)
    image = models.ImageField(null=True, upload_to="user_img")

    def is_available(self):
        if self.post_user.exists():
            return False
        else:
            return True

    def __unicode__(self):
        return u"{}".format(self.item)


class Renter(models.Model):
    name = models.ForeignKey(User, related_name='renter')
    rentals = models.ForeignKey(Item, related_name='items')

    def __unicode__(self):
        return u"{}".format(self.name)


class Review(models.Model):
    subject = models.CharField(max_length=150)

    user = models.ForeignKey(User, related_name="user_review")
    item = models.ForeignKey(Item, related_name="reviewed_item")
    text = models.CharField(max_length=3000)

    def __unicode__(self):
        return u"{}".format(self.subject)