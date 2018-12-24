from django.shortcuts import render
from django.views.generic import View
from .forms import *
from django.shortcuts import redirect
from .models import *

# Create your views here.


def index_backup(request):
    return render(request, 'backup/index_backup.html')

class general_settings_create(View):

    def get(self, request):
        form = general_settings()
        client_form= settings_client()
        storage_form = settings_storage()
        return render(request, 'backup/backup_general_settings.html', context={'form': form, 'client_form': client_form, 'storage_form': storage_form})

    def post(self, request):
        button_form = general_settings(request.POST)

        if button_form.is_valid():
            new_settings=button_form.save()
            return redirect(new_settings)
        return redirect(request, 'backup/backup_general_settings.html', context={'form': button_form})
