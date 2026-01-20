from django.contrib import admin
from .models import Moped

@admin.register(Moped)
class MopedAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'motor', 'starter')
    search_fields = ('name', 'body')
    list_filter = ('body', 'starter')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'body', 'motor', 'starter')
        }),
        ('Зображення', {
            'fields': ('image',)
        }),
    )

