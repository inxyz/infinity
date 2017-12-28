from django.contrib import admin

from oo.meta.models import Type, Instance
from oo.meta.forms import TypeForm, InstanceForm


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    form = TypeForm


@admin.register(Instance)
class InstanceModelAdmin(admin.ModelAdmin):
    form = InstanceForm

