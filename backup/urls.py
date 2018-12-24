from django.urls import path
from .views import *

urlpatterns = [
path('', index_backup, name='index_backup'),
path('general_settings/', general_settings_create.as_view(), name='general_settings')
    ]
