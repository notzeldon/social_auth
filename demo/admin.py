from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from demo.models import DemoUser

admin.site.register(DemoUser, UserAdmin)
