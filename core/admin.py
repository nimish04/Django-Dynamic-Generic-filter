from django.contrib import admin
from .models import Profile,Package,PackageAttribute,AttributeChoiceValue
# Register your models here.
admin.site.register(Package)
admin.site.register(PackageAttribute)
admin.site.register(AttributeChoiceValue)
