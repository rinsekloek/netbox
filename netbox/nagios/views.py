from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django_tables2 import RequestConfig

from dcim.models import Device
from dcim.tables import DeviceTable
from extras.views import ObjectConfigContextView
from utilities.views import (
    BulkCreateView, BulkDeleteView, BulkEditView, BulkImportView, ObjectDeleteView, ObjectEditView, ObjectListView,
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

# Nagios ContactGroup

class NagiosContactGroupListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'nagios.view_NagiosContactGroup'
    queryset = NagiosContactGroup.objects.annotate(nagioscontactgroup_count=Count('id'))
    table = tables.NagiosContactGroupTable
    template_name = 'nagios/nagioscontactgroup_list.html'


class NagiosContactGroupCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'nagios.add_nagioscontactgroup'
    model = NagiosContactGroup
    model_form = forms.NagiosContactGroupForm
    default_return_url = 'nagios:nagioscontactgroup_list'


class NagiosContactGroupEditView(NagiosContactGroupCreateView):
    permission_required = 'nagios.change_nagioscontactgroup'


class NagiosContactGroupBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'nagios.add_NagiosContactGroup'
    model_form = forms.NagiosContactGroupCSVForm
    table = tables.NagiosContactGroupTable
    default_return_url = 'nagios:nagioscontactgroup_list'


class NagiosContactGroupBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'nagios.delete_NagiosContactGroup'
    queryset = NagiosContactGroup.objects.annotate(nagioscontactgroup_count=Count('id'))
    table = tables.NagiosContactGroupTable
    default_return_url = 'nagios:nagioscontactgroup_list'
    
    
# Nagios HostGroup

class NagiosHostGroupListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'nagios.view_NagiosHostGroup'
    queryset = NagiosHostGroup.objects.annotate(nagioshostgroup_count=Count('id'))
    table = tables.NagiosHostGroupTable
    template_name = 'nagios/nagioshostgroup_list.html'


class NagiosHostGroupCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'nagios.add_nagioshostgroup'
    model = NagiosHostGroup
    model_form = forms.NagiosHostGroupForm
    default_return_url = 'nagios:nagioshostgroup_list'


class NagiosHostGroupEditView(NagiosHostGroupCreateView):
    permission_required = 'nagios.change_nagioshostgroup'


class NagiosHostGroupBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'nagios.add_NagiosHostGroup'
    model_form = forms.NagiosHostGroupCSVForm
    table = tables.NagiosHostGroupTable
    default_return_url = 'nagios:nagioshostgroup_list'


class NagiosHostGroupBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'nagios.delete_NagiosHostGroup'
    queryset = NagiosHostGroup.objects.annotate(nagioshostgroup_count=Count('id'))
    table = tables.NagiosHostGroupTable
    default_return_url = 'nagios:nagioshostgroup_list'
  
    
# Nagios Service

class NagiosServiceListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'nagios.view_NagiosService'
    queryset = NagiosService.objects.annotate(nagiosservice_count=Count('id'))
    table = tables.NagiosServiceTable
    template_name = 'nagios/nagiosservice_list.html'

    
class NagiosServiceView(PermissionRequiredMixin, View):
    permission_required = 'nagios.view_nagiosservice'

    def get(self, request, pk):
    
        nagiosservice = get_object_or_404(NagiosService, pk=pk)
        
        return render(request, 'nagios/nagiosservice.html', {
            'nagiosservice': nagiosservice,
        })


class NagiosServiceCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'nagios.add_nagiosservice'
    model = NagiosService
    model_form = forms.NagiosServiceForm
    template_name = 'nagios/nagiosservice_edit.html'
    
    def alter_obj(self, obj, request, url_args, url_kwargs):
        if 'device' in url_kwargs:
            obj.device = get_object_or_404(Device, pk=url_kwargs['device'])
        return obj

        
    def get_return_url(self, request, nagiosservice):
        if nagiosservice.parent:
            return nagiosservice.parent.get_absolute_url()


class NagiosServiceEditView(NagiosServiceCreateView):
    permission_required = 'nagios.change_nagiosservice'

    
class NagiosServiceDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'nagios.delete_nagiosservice'
    model = NagiosService


class NagiosServiceBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'nagios.add_NagiosService'
    model_form = forms.NagiosServiceCSVForm
    table = tables.NagiosServiceTable
    default_return_url = 'nagios:nagiosservice_list'


class NagiosServiceBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'nagios.delete_NagiosService'
    queryset = NagiosService.objects.annotate(nagiosservice_count=Count('id'))
    table = tables.NagiosServiceTable
    default_return_url = 'nagios:nagiosservice_list'


# Nagios Platform

class NagiosPlatformListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'nagios.view_NagiosPlatform'
    queryset = NagiosPlatform.objects.annotate(nagiosplatform_count=Count('id'))
    table = tables.NagiosPlatformTable
    template_name = 'nagios/nagiosplatform_list.html'


class NagiosPlatformCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'nagios.add_nagiosplatform'
    model = NagiosPlatform
    model_form = forms.NagiosPlatformForm
    default_return_url = 'nagios:nagiosplatform_list'


class NagiosPlatformEditView(NagiosPlatformCreateView):
    permission_required = 'nagios.change_nagiosplatform'



class NagiosPlatformBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'nagios.add_NagiosPlatform'
    model_form = forms.NagiosPlatformCSVForm
    table = tables.NagiosPlatformTable
    default_return_url = 'nagios:nagiosplatform_list'


class NagiosPlatformBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'nagios.delete_NagiosPlatform'
    queryset = NagiosPlatform.objects.annotate(nagiosplatform_count=Count('id'))
    table = tables.NagiosPlatformTable
    default_return_url = 'nagios:nagiosplatform_list'




