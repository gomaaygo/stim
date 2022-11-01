from django.contrib import admin

from .models import AQChild

@admin.register(AQChild)
class AQChildAdmin(admin.ModelAdmin):
    pass