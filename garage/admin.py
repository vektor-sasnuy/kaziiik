from django.contrib import admin
from .models import Garage, GarageItem


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(GarageItem)
class GarageItemAdmin(admin.ModelAdmin):
    list_display = ('get_vehicle_name', 'vehicle_type', 'garage', 'added_date')
    list_filter = ('vehicle_type', 'garage')
    
    def get_vehicle_name(self, obj):
        return obj.__str__()
    get_vehicle_name.short_description = 'Vehicle'
