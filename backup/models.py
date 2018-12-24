from django.db import models
from backup.mixins.mixin_models import *

# Файл для создания моделей (стркутур) таблиц в базе данных postgreeSQL

class backups_settings_template(models.Model):
    '''Класс таблицы организации общего шаблона для резервного копирования'''

    class Meta():
        db_table = 'backups_settigs_template'
        verbose_name = 'Настройки резервного копирования'

    name_template = models.CharField('Имя шаблона', max_length=100)
    lead_time = models.TimeField('время начала копирования')
    completion_time = models.TimeField('Время завершения копирования')
    command_backups = models.CharField('команда для копирования', max_length=1500)
    report_formation = models.BooleanField('Формировать отчет')
    email_report = models.EmailField('email адрес')
    date_create = models.DateTimeField('Дата создания шаблона', auto_now_add=True)
    date_upgrade = models.DateTimeField('Дата изменения', auto_now=True)


def __str__(self):
    return self.name_temlate




class client_backup(models.Model):
#'''Модель для таблицы клиенских ПК из которых будет копироваться информация'''
    class Meta:
        verbose_name = 'Клиент'

    name = models.CharField('Имя', max_length=100)
    ip = models.GenericIPAddressField('ip адрес', protocol='IPv4')
    dir = models.CharField('Путь к катологу', max_length=1500)
    mount = models.CharField('монтирование каталога', max_length=1500)
    umount = models.CharField('размонтирование каталога', max_length=1500)
    mount_time = models.TimeField('время монтирования каталога', auto_now=True)
    umount_time = models.TimeField('время размонтирования каталога', auto_now=True)
    date_create = models.DateTimeField('дата создания записи', auto_now_add=True)
    mount_chekbox = models.BooleanField('Монтировать')
    umount_chekbox = models.BooleanField('Размотнировать')







class storge_backup(models.Model):
#'''Модель файлового хранилища, куда будет копироваться информация'''
    class Meta:
        verbose_name = 'хранилище'

    name = models.CharField('Имя', max_length=100)
    ip = models.GenericIPAddressField('ip адрес', protocol='IPv4')
    dir = models.CharField('Путь к катологу', max_length=1500)
    mount = models.CharField('монтирование каталога', max_length=1500)
    umount = models.CharField('размонтирование каталога', max_length=1500)
    mount_time = models.TimeField('время монтирования каталога', auto_now=True)
    umount_time = models.TimeField('время размонтирования каталога', auto_now=True)
    date_create = models.DateTimeField('дата создания записи', auto_now_add=True)
    mount_chekbox = models.BooleanField('Монтировать')
    umount_chekbox = models.BooleanField('Размотнировать')
