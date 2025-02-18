from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','email','birth_data','photo']
    raw_id_fields = ['user']