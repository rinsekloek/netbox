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


@admin.register(NagiosContactGroup, site=admin_site)
class NagiosContactGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias']
    fields = ['name', 'alias']


@admin.register(NagiosService, site=admin_site)
class NagiosServiceAdmin(admin.ModelAdmin):
    list_display = ['name','device']
    fields = ['name','use_template','device','service_description','active_checks_enabled','passive_checks_enabled','check_command','check_command_params','max_check_attempts','normal_check_interval','retry_check_interval','notification_interval','notification_period','notification_options','notifications_enabled','check_period','event_handler','contact_groups']



    




