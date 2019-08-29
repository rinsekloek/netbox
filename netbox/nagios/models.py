# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from dcim.models import *
from extras.models import ConfigContextModel, CustomFieldModel, TaggedItem
from utilities.models import ChangeLoggedModel


class NagiosCheck(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    check_name = models.CharField(max_length=255)
    check_command = models.CharField(max_length=512)
    performance_value = models.CharField(max_length=255)
    
    csv_headers = ['check_name', 'check_command']

    class Meta:
        managed = True
        db_table = 'nagios_checks'
        
    def __str__(self):
        return '%s ' % (self.check_name)
    


class NagiosContactgroup(ChangeLoggedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=255)
    
    csv_headers = ['name', 'alias']

    class Meta:
        managed = True
        db_table = 'nagios_contactgroups'
        
    def __str__(self):
        return '%s ' % (self.name)


class NagiosContact(ChangeLoggedModel):
    id = models.IntegerField(primary_key=True)
    alias = models.CharField(max_length=255)
    
    csv_headers = ['alias', 'email']
    
    service_notification_period = models.ForeignKey('NagiosTimeperiods', models.DO_NOTHING, db_column='service_notification_period', related_name='service_notification_period')
    host_notification_period = models.ForeignKey('NagiosTimeperiods', models.DO_NOTHING, db_column='host_notification_period', related_name='host_notification_period')
    
    service_notification_options = models.CharField(max_length=64)
    host_notification_options = models.CharField(max_length=64)
    service_notification_commands = models.CharField(max_length=255)
    host_notification_commands = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pager = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'nagios_contacts'
        
    def __str__(self):
        return '%s ' % (self.alias)



class NagiosHostgroups(ChangeLoggedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=255)
    platform = models.ForeignKey('NagiosPlatforms', models.DO_NOTHING, db_column='platform', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nagios_hostgroups'


class NagiosHosttemplates(ChangeLoggedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    use_template = models.IntegerField(blank=True, null=True)
    check_command = models.ForeignKey(NagiosCheck, models.DO_NOTHING, db_column='check_command', blank=True, null=True)
    max_check_attempts = models.SmallIntegerField(blank=True, null=True)
    notification_interval = models.SmallIntegerField(blank=True, null=True)
    notification_period = models.ForeignKey('NagiosTimeperiods', models.DO_NOTHING, db_column='notification_period', blank=True, null=True)
    notification_options = models.CharField(max_length=64, blank=True, null=True)
    notifications_enabled = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nagios_hosttemplates'


class NagiosServers(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    naam = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    user = models.CharField(max_length=64)
    pass_field = models.CharField(db_column='pass', max_length=64)  # Field renamed because it was a Python reserved word.
    configpath_remote = models.CharField(max_length=255)
    configpath_local = models.CharField(max_length=255)
    initscript = models.CharField(max_length=255)
    platform = models.ForeignKey('NagiosPlatforms', models.DO_NOTHING, db_column='platform', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nagios_servers'


class NagiosTimeperiods(ChangeLoggedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=255)
    timespan = models.TextField()

    class Meta:
        managed = True
        db_table = 'nagios_timeperiods'

    def __str__(self):
        return '%s ' % (self.name)

class NagiosService(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    use_template = models.IntegerField(blank=True, null=True)
    server = models.ForeignKey('dcim.Device', models.DO_NOTHING, db_column='server', blank=True, null=True, related_name='server')
    service_description = models.CharField(max_length=255)
    active_checks_enabled = models.SmallIntegerField(blank=True, null=True)
    passive_checks_enabled = models.SmallIntegerField(blank=True, null=True)
    check_command = models.ForeignKey(NagiosCheck, models.DO_NOTHING, db_column='check_command')
    check_command_params = models.CharField(max_length=255)
    max_check_attempts = models.IntegerField(blank=True, null=True)
    normal_check_interval = models.IntegerField(blank=True, null=True)
    retry_check_interval = models.IntegerField(blank=True, null=True)
    notification_interval = models.SmallIntegerField(blank=True, null=True)
    notification_period = models.ForeignKey(NagiosTimeperiods, models.DO_NOTHING, db_column='notification_period', blank=True, null=True, related_name='notification_period' )
    notification_options = models.CharField(max_length=64, blank=True, null=True)
    notifications_enabled = models.SmallIntegerField(blank=True, null=True)
    check_period = models.ForeignKey(NagiosTimeperiods, models.DO_NOTHING, db_column='check_period', related_name='check_period')
    event_handler = models.CharField(max_length=255, blank=True, null=True)
    contact_groups = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'nagios_services'
    
    def __str__(self):
        return '%s ' % (self.name)


class NagiosContactgroupsMember(ChangeLoggedModel):
    contact = models.ForeignKey(NagiosContact, models.DO_NOTHING, db_column='contact', blank=True, null=True)
    contactgroup = models.ForeignKey(NagiosContactgroup, models.DO_NOTHING, db_column='contactgroup', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nagios_contactgroups_members'
        unique_together = (('contact', 'contactgroup'),)



class NagiosServicesContactgroups(ChangeLoggedModel):
    service = models.ForeignKey(NagiosService, models.DO_NOTHING, db_column='service', blank=True, null=True)
    contactgroup = models.ForeignKey(NagiosContactgroup, models.DO_NOTHING, db_column='contactgroup', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nagios_services_contactgroups'
        unique_together = (('service', 'contactgroup'),)


class NagiosPlatforms(ChangeLoggedModel):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nagios_platforms'
