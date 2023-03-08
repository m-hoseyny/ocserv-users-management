from django.contrib import admin

from .models import *

admin.site.register(OcservUser)
# Register your models here.

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']