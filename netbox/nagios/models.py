from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.db.models.expressions import RawSQL
from django.urls import reverse
from taggit.managers import TaggableManager

from dcim.models import *
# from extras.models import CustomFieldModel, ObjectChange
from utilities.models import ChangeLoggedModel
from utilities.utils import serialize_object



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
        return '%s' % (self.check_name)
    


class NagiosContact(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    alias = models.CharField(max_length=255)
    service_notification_period = models.ForeignKey('NagiosTimePeriod', models.DO_NOTHING, db_column='service_notification_period', related_name='service_notification_period')
    host_notification_period = models.ForeignKey('NagiosTimePeriod', models.DO_NOTHING, db_column='host_notification_period', related_name='host_notification_period')
    
    service_notification_options = models.CharField(max_length=64)
    host_notification_options = models.CharField(max_length=64)
    service_notification_commands = models.CharField(max_length=255)
    host_notification_commands = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pager = models.CharField(max_length=255)
    
    csv_headers = ['alias', 'email']
    
    class Meta:
        managed = True
        db_table = 'nagios_contacts'
        
    def __str__(self):
        #return '%s ' % (self.alias)
        return self.name()
        
    def name(self):
        return '%s' % (self.alias.replace(" ", "_").replace("-", "_").lower())
        
    #def get_absolute_url(self):
        #return reverse('nagios:nagioscontact', args=[self.pk])
        

class NagiosContactGroup(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=255)
    
    contacts = models.ManyToManyField(NagiosContact)
    
    csv_headers = ['name', 'alias', 'contacts']

    class Meta:
        managed = True
        db_table = 'nagios_contactgroups'
        
    def __str__(self):
        return '%s' % (self.name)
        


class NagiosHostGroup(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=255)
    #platform = models.ForeignKey('NagiosPlatform', models.DO_NOTHING, db_column='platform', blank=True, null=True)
    platform = models.ForeignKey(to='dcim.Platform', on_delete=models.CASCADE, db_column='platform', blank=True, null=True, related_name='nagioshostgroup', verbose_name='platform')

    csv_headers = ['id','name', 'alias', 'platform']
    
    class Meta:
        managed = True
        db_table = 'nagios_hostgroups'
        
    def __str__(self):
        return '%s' % (self.name)


class NagiosHostTemplate(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    use_template = models.ForeignKey('self', on_delete=models.CASCADE, db_column='use_template', null=True, blank=True, verbose_name='Inherits from template')
    check_command = models.ForeignKey(NagiosCheck, models.DO_NOTHING, db_column='check_command', blank=True, null=True)
    max_check_attempts = models.SmallIntegerField(blank=True, null=True)
    notification_interval = models.SmallIntegerField(blank=True, null=True)
    notification_period = models.ForeignKey('NagiosTimePeriod', models.DO_NOTHING, db_column='notification_period', blank=True, null=True)
    notification_options = models.CharField(max_length=64, blank=True, null=True)
    notifications_enabled = models.SmallIntegerField(blank=True, null=True)

    csv_headers = ['name', 'use_template', 'check_command']
    
    class Meta:
        managed = True
        db_table = 'nagios_hosttemplates'
        
    def __str__(self):
        return '%s' % (self.name)

class NagiosTimePeriod(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=255)
    timespan = models.TextField()

    csv_headers = ['name', 'alias', 'timespan']
    
    class Meta:
        managed = True
        db_table = 'nagios_timeperiods'

    def __str__(self):
        return '%s' % (self.name)

class NagiosService(ChangeLoggedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Template name', blank=True, null=True)
    use_template = models.ForeignKey('self', on_delete=models.CASCADE, db_column='use_template', null=True, blank=True, verbose_name='Inherits from template')
    device = models.ForeignKey(to='dcim.Device', on_delete=models.CASCADE, db_column='server', blank=True, null=True, related_name='nagiosservices', verbose_name='device'  )
    service_description = models.CharField(max_length=255,verbose_name='Service Description')
    active_checks_enabled = models.BooleanField(blank=True, null=True)
    passive_checks_enabled = models.BooleanField(blank=True, null=True)
    check_command = models.ForeignKey(NagiosCheck, models.DO_NOTHING, db_column='check_command', blank=True, null=True)
    check_command_params = models.CharField(max_length=255, blank=True, null=True)
    max_check_attempts = models.IntegerField(blank=True, null=True)
    normal_check_interval = models.IntegerField(blank=True, null=True)
    retry_check_interval = models.IntegerField(blank=True, null=True)
    notification_interval = models.SmallIntegerField(blank=True, null=True)
    notification_period = models.ForeignKey(NagiosTimePeriod, models.DO_NOTHING, db_column='notification_period', blank=True, null=True, related_name='notification_period' )
    notification_options = models.CharField(max_length=64, blank=True, null=True)
    notifications_enabled = models.BooleanField(blank=True, null=True)
    check_period = models.ForeignKey(NagiosTimePeriod, models.DO_NOTHING, db_column='check_period', related_name='check_period', blank=True, null=True)
    event_handler = models.CharField(max_length=255, blank=True, null=True)
    contact_groups = models.ManyToManyField(NagiosContactGroup)  

    csv_headers = ['id', 'name', 'device']
    
    class Meta:
        managed = True
        db_table = 'nagios_services'
    
    def __str__(self):
        return '%s' % (self.name)
        
    def get_absolute_url(self):
        return reverse('nagios:nagiosservice', args=[self.pk])
        
    def to_csv(self):
        return (
            self.pk,
            self.name,
            self.device
        )
        
    @property
    def parent(self):
        return self.device
           
            
