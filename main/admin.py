from django.contrib import admin
from .models import Location, Urn, TypesUrn, User

admin.site.register(Location)
admin.site.register(Urn)
admin.site.register(TypesUrn)
admin.site.register(User)