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



