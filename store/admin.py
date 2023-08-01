from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Product)
class AdminCategory(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Slider)
class AdminCategory(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Author)
class AdminCategory(admin.ModelAdmin):
    list_per_page = 20