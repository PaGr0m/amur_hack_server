from django.contrib import admin
from .models import Location, Trashcan, Urn, User


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


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "login", "nickname", "fio", "score"]

    class Meta:
        model = User


admin.site.register(Location, LocationAdmin)
admin.site.register(Trashcan, TrashcanAdmin)
admin.site.register(Urn, UrnAdmin)
admin.site.register(User, UserAdmin)
