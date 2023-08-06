from django.contrib import admin
from .models import short_url , server_counter
# Register your models here.

admin.site.register(short_url)
admin.site.register(server_counter)