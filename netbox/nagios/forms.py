from django import forms
from django.core.exceptions import ValidationError
from taggit.forms import TagField

from dcim.forms import INTERFACE_MODE_HELP_TEXT
from dcim.models import Device
#from extras.forms import AddRemoveTagsForm, CustomFieldBulkEditForm, CustomFieldForm, CustomFieldFilterForm
from ipam.models import IPAddress
from utilities.forms import (
    add_blank_choice, APISelect, APISelectMultiple, BootstrapMixin, BulkEditForm, BulkEditNullBooleanSelect,
    ChainedFieldsMixin, ChainedModelChoiceField, ChainedModelMultipleChoiceField, CommentField, ComponentForm,
    ConfirmationForm, CSVChoiceField, ExpandableNameField, FilterChoiceField, JSONField, SlugField,
    SmallTextarea, StaticSelect2, StaticSelect2Multiple
)
from .models import *

#
# NagiosChecks
#

class NagiosCheckForm(BootstrapMixin, forms.ModelForm):
    
    class Meta:
        model = NagiosCheck
        fields = [
            'check_name', 'check_command',
        ]


class NagiosCheckCSVForm(forms.ModelForm):

    class Meta:
        model = NagiosCheck
        fields = NagiosCheck.csv_headers
        help_texts = {
            'check_name': 'Name of check',
            'check_command': 'Full command of check including $ARGS$',
        }

        
# Nagios Contact
        
class NagiosContactForm(BootstrapMixin, forms.ModelForm):
    
    class Meta:
        model = NagiosContact
        fields = [
            'alias', 'email', 'pager', 'service_notification_period', 'host_notification_period',  'service_notification_options', 'host_notification_options', 'service_notification_commands', 'host_notification_commands', 
        ]



class NagiosContactCSVForm(forms.ModelForm):

    class Meta:
        model = NagiosContact
        fields = NagiosContact.csv_headers
        help_texts = {
            'alias': 'Name of the contact person',
            'email': 'E-mail address    ',
        }
        
# Nagios ContactGroup

class NagiosContactGroupForm(BootstrapMixin, forms.ModelForm):
    
    class Meta:
        model = NagiosContactGroup
        fields = [
            'name', 'alias','contacts'
        ]



class NagiosContactGroupCSVForm(forms.ModelForm):

    class Meta:
        model = NagiosContactGroup
        fields = NagiosContactGroup.csv_headers
        help_texts = {
            'name': 'Name of the contactgroup',
            'alias': 'Extended name of the contacgroup',
        }       

        
# Nagios ContactGroup

class NagiosHostGroupForm(BootstrapMixin, forms.ModelForm):
    
    class Meta:
        model = NagiosHostGroup
        fields = [
            'name', 'alias','platform'
        ]



class NagiosHostGroupCSVForm(forms.ModelForm):

    class Meta:
        model = NagiosHostGroup
        fields = NagiosHostGroup.csv_headers
        help_texts = {
            'name': 'Name of the contactgroup',
            'alias': 'Extended name of the contacgroup',
        }       
 


# Nagios Service        
        
class NagiosServiceForm(BootstrapMixin, forms.ModelForm):
    
    class Meta:
        model = NagiosService
        fields = [
            'id', 'name', 'use_template', 'device', 'service_description', 'active_checks_enabled', 
            'passive_checks_enabled', 'check_command', 'check_command_params', 'max_check_attempts', 
            'normal_check_interval', 'retry_check_interval', 'notification_interval', 'notification_period', 
            'notification_options','notifications_enabled', 'check_period', 'event_handler', 'contact_groups'                  
        ]



class NagiosServiceCSVForm(forms.ModelForm):

    class Meta:
        model = NagiosService
        fields = NagiosService.csv_headers
        help_texts = {
            'name': 'Name of the service',
            'device': 'Device',
        }
        
        
# Nagios Platform     

class NagiosPlatformForm(BootstrapMixin, forms.ModelForm):
    
    class Meta:
        model = NagiosPlatform
        fields = [
            'name'
        ]



class NagiosPlatformCSVForm(forms.ModelForm):

    class Meta:
        model = NagiosPlatform
        fields = NagiosPlatform.csv_headers
        help_texts = {
            'name': 'Name of the platform',
        }       
 



