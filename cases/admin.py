from django.contrib import admin
from .models import Case, CaseReward, OpenedCase


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'price', 'is_active', 'created_at')
    list_filter = ('rarity', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)


@admin.register(CaseReward)
class CaseRewardAdmin(admin.ModelAdmin):
    list_display = ('case', 'vehicle_type', 'get_vehicle_name', 'probability')
    list_filter = ('case', 'vehicle_type', 'probability')
    search_fields = ('case__name',)
    
    def get_vehicle_name(self, obj):
        vehicle = obj.get_vehicle()
        return vehicle.name if vehicle else 'None'
    get_vehicle_name.short_description = 'Vehicle'


@admin.register(OpenedCase)
class OpenedCaseAdmin(admin.ModelAdmin):
    list_display = ('case', 'get_reward_vehicle', 'opened_at')
    list_filter = ('case', 'opened_at')
    search_fields = ('case__name',)
    readonly_fields = ('case', 'reward', 'opened_at')
    
    def get_reward_vehicle(self, obj):
        if obj.reward:
            vehicle = obj.reward.get_vehicle()
            return vehicle.name if vehicle else 'None'
        return 'No reward'
    get_reward_vehicle.short_description = 'Reward'
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
