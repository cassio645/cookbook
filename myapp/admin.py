from django.contrib import admin
from .models import Receita, Categoria
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

class MyModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass

admin.site.register(Receita, MyModelAdmin)
admin.site.register(Categoria)