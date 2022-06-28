from django.contrib import admin

# Register your models here.
from .models import product,user

admin.site.register(product)
admin.site.register(user)