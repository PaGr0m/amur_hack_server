from django.contrib import admin
from .models import Location, Urn, User

admin.site.register(Location)
class UrnAdmin(admin.ModelAdmin):
    list_display = ('location', 'trash_type', 'UUID')

admin.site.register(Urn, UrnAdmin)
admin.site.register(User)
