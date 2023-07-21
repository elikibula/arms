from django.contrib import admin
from .models import Arm, ArmIssue, Location

@admin.register(Arm)
class ArmAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'serial_number', 'status', 'location')


@admin.register(ArmIssue)
class ArmIssueAdmin(admin.ModelAdmin):
    list_display = ('arm_type','serial_number', 'name', 'regimental_number', 'rank')
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

