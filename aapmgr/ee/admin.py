from django.contrib import admin

# Register your models here.
from .models import EEDefinition, PipPackage, AnsibleCollection, AnsibleRole, RedhatRepository
from django.shortcuts import render



admin.site.register(EEDefinition)
admin.site.register(PipPackage)
admin.site.register(AnsibleCollection)
admin.site.register(AnsibleRole)
admin.site.register(RedhatRepository)