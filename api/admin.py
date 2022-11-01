from django.contrib import admin

from .models import AQChild, Person

@admin.register(AQChild)
class AQChildAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass