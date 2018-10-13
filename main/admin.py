from django.contrib import admin
from .models import Location, Urn, User, Trashcan


# class UrnAdmin(admin.ModelAdmin):
#     list_display = ('location', 'trash_type', 'UUID')

# admin.site.register(Urn, UrnAdmin)

admin.site.register(Trashcan)
admin.site.register(Urn)
admin.site.register(Location)
admin.site.register(User)
