from django.contrib import admin
<<<<<<< HEAD
from .models import Location, Urn, Client
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
=======
from .models import Location, Trashcan, Urn, User


class LocationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "longitude", "latitude"]

    class Meta:
        model = Location


class TrashcanAdmin(admin.ModelAdmin):
    list_display = ["id", "location"]

    class Meta:
        model = Trashcan

>>>>>>> pagrom

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
<<<<<<< HEAD

class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'пользователи'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline,)

# Re-register UserAdmin
admin.site.unregister(User)
=======
>>>>>>> pagrom
admin.site.register(User, UserAdmin)
