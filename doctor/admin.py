from django.contrib import admin
from .models import Doctor, Direction

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'sort_order')
    search_fields = ('name',)
    ordering = ('sort_order',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'experience', 'sort_order')
    search_fields = ('name',)
    list_filter = ('directions', 'experience')
    ordering = ('sort_order', 'name')
    filter_horizontal = ('directions',)
