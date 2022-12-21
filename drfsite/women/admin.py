from django.contrib import admin
from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'time_create', 'time_update', 'is_publish')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
