from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(backups_settings_template)
admin.site.register(client_backup)
admin.site.register(storge_backup)
