from django import forms
from django.db import models
from django.db.models import Q

pri = (
    ((0, 999), 'Rs 0-999'),
    ((1000, 2499), 'Rs 1000-2499'),
    ((2500, 10000), 'Rs 2500-10000'),
    ((10001, 50000), 'Rs 10001-50K'),
    ((500001,1000000),'Rs 50K+'),
)

people=(
    ((1,5), '1-5'),
    ((6,10), '6-10'),
    ((11, 20), '11-20'),
    ((21,1000), '20+'),
)

class Att2(models.Model):
    type = models.CharField(
        choices=pri, max_length=100)
    type=models.CharField(choices=people, max_length=100)
