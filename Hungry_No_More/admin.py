from django.contrib import admin

from .models import FoodDetails,User,NGO,Vendor
# Register your models here.
admin.site.register(User)
admin.site.register(FoodDetails)
admin.site.register(NGO)
admin.site.register(Vendor)