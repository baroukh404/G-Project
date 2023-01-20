from django.contrib import admin
from .models import users

class UserLists(admin.ModelAdmin):
	list_display = ('Firstname', 'Lastname', 'Phone', 'Email', 'Filiere', 'Parcours')

admin.site.register(users, UserLists)
