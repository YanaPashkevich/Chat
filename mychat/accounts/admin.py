from django.contrib import admin

# Register your models here.

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography', 'date_of_birth', 'photo')


admin.site.register(Profile, ProfileAdmin)