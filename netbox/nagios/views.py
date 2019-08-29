from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import View

from dcim.models import Device, Interface
from dcim.tables import DeviceTable
from extras.views import ObjectConfigContextView
from ipam.models import Service
from utilities.views import (
    BulkComponentCreateView, BulkDeleteView, BulkEditView, BulkImportView, ComponentCreateView, ObjectDeleteView,
    ObjectEditView, ObjectListView,
)
from . import forms, tables
from .models import *


# Nagios Checks

class NagiosCheckListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'nagios.view_NagiosCheck'
    queryset = NagiosCheck.objects.annotate(nagioscheck_count=Count('id'))
    table = tables.NagiosCheckTable
    template_name = 'nagios/nagioscheck_list.html'


class NagiosCheckCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'nagios.add_nagioscheck'
    model = NagiosCheck
    model_form = forms.NagiosCheckForm
    default_return_url = 'nagios:nagioscheck_list'


class NagiosCheckEditView(NagiosCheckCreateView):
    permission_required = 'nagios.change_nagioscheck'


class NagiosCheckBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'nagios.add_NagiosCheck'
    model_form = forms.NagiosCheckCSVForm
    table = tables.NagiosCheckTable
    default_return_url = 'nagios:nagioscheck_list'


class NagiosCheckBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'nagios.delete_NagiosCheck'
    queryset = NagiosCheck.objects.annotate(nagioscheck_count=Count('id'))
    table = tables.NagiosCheckTable
    default_return_url = 'nagios:nagioscheck_list'
    
# Nagios Contacts

class NagiosContactListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'nagios.view_NagiosContact'
    queryset = NagiosContact.objects.annotate(nagioscontact_count=Count('id'))
    table = tables.NagiosContactTable
    template_name = 'nagios/nagioscontact_list.html'


class NagiosContactCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'nagios.add_nagioscontact'
    model = NagiosContact
    model_form = forms.NagiosContactForm
    default_return_url = 'nagios:nagioscontact_list'


class NagiosContactEditView(NagiosContactCreateView):
    permission_required = 'nagios.change_nagioscontact'


class NagiosContactBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'nagios.add_NagiosContact'
    model_form = forms.NagiosContactCSVForm
    table = tables.NagiosContactTable
    default_return_url = 'nagios:nagioscontact_list'


class NagiosContactBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'nagios.delete_NagiosContact'
    queryset = NagiosContact.objects.annotate(nagioscontact_count=Count('id'))
    table = tables.NagiosContactTable
    default_return_url = 'nagios:nagioscontact_list'


