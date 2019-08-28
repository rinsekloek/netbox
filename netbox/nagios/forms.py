from django import forms
from django.core.exceptions import ValidationError
from taggit.forms import TagField

from dcim.constants import IFACE_TYPE_VIRTUAL, IFACE_MODE_ACCESS, IFACE_MODE_TAGGED_ALL
from dcim.forms import INTERFACE_MODE_HELP_TEXT
from dcim.models import Device, DeviceRole, Interface, Platform, Rack, Region, Site
from extras.forms import AddRemoveTagsForm, CustomFieldBulkEditForm, CustomFieldForm, CustomFieldFilterForm
from ipam.models import IPAddress
from utilities.forms import (
    add_blank_choice, APISelect, APISelectMultiple, BootstrapMixin, BulkEditForm, BulkEditNullBooleanSelect,
    ChainedFieldsMixin, ChainedModelChoiceField, ChainedModelMultipleChoiceField, CommentField, ComponentForm,
    ConfirmationForm, CSVChoiceField, ExpandableNameField, FilterChoiceField, JSONField, SlugField,
    SmallTextarea, StaticSelect2, StaticSelect2Multiple
)
#from .constants import VM_STATUS_CHOICES
from .models import *

VIFACE_TYPE_CHOICES = (
    (IFACE_TYPE_VIRTUAL, 'Virtual'),
)


#
# NagiosChecks
#

class NagiosCheckForm(BootstrapMixin, forms.ModelForm):
    slug = SlugField()

    class Meta:
        model = NagiosCheck
        fields = [
            'check_name', 'check_command',
        ]


class NagiosCheckCSVForm(forms.ModelForm):
    slug = SlugField()

    class Meta:
        model = NagiosCheck
        fields = NagiosCheck.csv_headers
        help_texts = {
            'check_name': 'Name of cluster type',
        }


