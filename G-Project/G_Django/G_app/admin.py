from django.contrib import admin
from .models import user, group


class ListUser(admin.ModelAdmin):
    list_display = ("Firstname", "Phone", "Email")

admin.site.register(user, ListUser)

class Status(admin.ModelAdmin):
    list_display = ("admin", "invite")

admin.site.register(group, Status)