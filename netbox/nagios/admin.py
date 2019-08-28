from django.contrib import admin, messages
from django.shortcuts import redirect, render

from .models import *
from dcim.models import *
from netbox.admin import admin_site

#admin.site.register(NagiosCheck)

@admin.register(NagiosCheck, site=admin_site)
class NagiosCheckAdmin(admin.ModelAdmin):
    list_display = ['check_name', 'check_command']
    fields = ['check_name', 'check_command']


@admin.register(NagiosContactgroup, site=admin_site)
class NagiosContactgroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias']
    fields = ['name', 'alias']


@admin.register(NagiosContactgroupsMember, site=admin_site)
class NagiosContactgroupsMemberAdmin(admin.ModelAdmin):
    list_display = ['contactgroup', 'contact']
    fields = ['contactgroup', 'contact']


@admin.register(NagiosService, site=admin_site)
class NagiosServiceAdmin(admin.ModelAdmin):
    list_display = ['name','server']
    fields = ['name','use_template','server','service_description','active_checks_enabled','passive_checks_enabled','check_command','check_command_params','max_check_attempts','normal_check_interval','retry_check_interval','notification_interval','notification_period','notification_options','notifications_enabled','check_period','event_handler','contact_groups']



    




