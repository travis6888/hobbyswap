from django.contrib import admin

# Register your models here.
from hobbyswap.models import Condition, Item, Renter, Category

admin.site.register(Condition)

admin.site.register(Item)
admin.site.register(Renter)
admin.site.register(Category)