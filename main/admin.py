from django.contrib import admin
from .models import Location, Trashcan, Urn, Client


class LocationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "longitude", "latitude"]

    class Meta:
        model = Location


class TrashcanAdmin(admin.ModelAdmin):
    list_display = ["id", "location"]

    class Meta:
        model = Trashcan


class UrnAdmin(admin.ModelAdmin):
    list_display = ["id", "trash_type", "workload", "trashcan"]
    list_filter = ["trash_type", "trashcan"]

    class Meta:
        model = Urn


class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "password", "token", "firstname", "surname", "phone", "score"]

    class Meta:
        model = Client


admin.site.register(Client, ClientAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Trashcan, TrashcanAdmin)
admin.site.register(Urn, UrnAdmin)
