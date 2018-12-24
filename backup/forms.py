from django import forms
from django.core.exceptions import ValidationError

from .models import *
from django.forms import ModelForm



class general_settings(ModelForm):

    class Meta:
        model = backups_settings_template
        fields = ('name_template', 'lead_time', 'report_formation', 'email_report')

    def clean_settings(self):
        new_seting = self.cleaned_data['name_template'].upper()

        if new_seting == 'create':
            raise ValidationError('Слово - "Create" является исключением, его нельзя использовать')
        return new_seting


    def save(self):
        new_settings = backups_settings_template.objects.create(
            name_template=self.cleaned_data['name_template'],
            load_time=self.cleaned_data['lead_time'],
            email_report=self.cleaned_data['email_report'],
            report_formation=self.cleaned_data['report_formation']
        )
        return new_settings




class settings_client(ModelForm):

    class Meta:
        model = client_backup
        fields = ('name', 'ip', 'dir', 'mount_chekbox', 'umount_chekbox')

    def clean_settings(self):
        new_client = self.cleaned_data['name'].upper()

        if new_client == 'create':
            raise ValidationError('Слово - "Create" является исключением, его нельзя использовать')
        return new_client

    def save(self):
        new_clients = client_backup.objects.create(
            name=self.cleaned_data['name'],
            ip=self.cleaned_data['ip'],
            dir=self.cleaned_data['dir'],
            mount_chekbox=self.cleaned_data['mount_chekbox'],
            umount_chekbox=self.cleaned_data['umount_chekbox']
        )
        return new_clients


class settings_storage(ModelForm):

    class Meta:
        model = storge_backup
        fields = ('name', 'ip', 'dir', 'mount_chekbox', 'umount_chekbox')

    def clean_settings(self):
        new_storage = self.cleaned_data['name'].upper()

        if new_storage == 'create':
            raise ValidationError('Слово - "Create" является исключением, его нельзя использовать')
        return new_storage

    def save(self):
        new_storages = client_backup.objects.create(
            name=self.cleaned_data['name'],
            ip=self.cleaned_data['ip'],
            dir=self.cleaned_data['dir'],
            mount_chekbox=self.cleaned_data['mount_chekbox'],
            umount_chekbox=self.cleaned_data['umount_chekbox']
        )
        return new_storages
