from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Notes)

#TODO: Register admin models Homework
admin.site.register(Homework)

#TODO: Register admin models Todo
admin.site.register(Todo)