from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxLengthValidator
from django.contrib.postgres.fields import HStoreField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Package(models.Model):
    name=models.CharField(max_length=200,unique=True,null=False)
    description=models.TextField(max_length=1000)
    #activities=models.TextField(max_length=800)
    #duration=models.CharField(max_length=100)
    location=models.CharField(max_length=100,null=False)
    #price=models.CharField(max_length=100)
    attributes = HStoreField(default={})
    other_inclusions=models.TextField(max_length=1000)
    itinerary=models.TextField(max_length=1000)
    things_to_carry=models.TextField(max_length=1000)
    availability=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PackageAttribute(models.Model):
    name=models.CharField(max_length=100)
    op=models.CharField(max_length=20,default='in')

    def __str__(self):
        return self.name

    def has_values(self):
        return self.values.exists()

class AttributeChoiceValue(models.Model):
    name=models.CharField(max_length=100)
    attribute=models.ForeignKey(PackageAttribute,related_name='values',on_delete=models.CASCADE)

    class Meta():
        unique_together=('name','attribute')

    def __str__(self):
        return self.name
