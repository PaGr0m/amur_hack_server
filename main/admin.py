from django.contrib import admin
from .models import Location, Urn, Client
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Location)
class UrnAdmin(admin.ModelAdmin):
    list_display = ('location', 'trash_type', 'UUID')

admin.site.register(Urn, UrnAdmin)

# class ClientInline(admin.StackedInline):
#     model = Client
#     can_delete = False
#     verbose_name_plural = 'пользователи'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ClientInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Client)