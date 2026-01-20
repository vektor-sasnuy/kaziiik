from django.contrib import admin
from .models import Cars

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'motor', 'gear_type')
    search_fields = ('name', 'body')
    list_filter = ('body', 'gear_type')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'body', 'motor', 'gear_type')
        }),
        ('Зображення', {
            'fields': ('image',)
        }),
    )

