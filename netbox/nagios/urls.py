from django.urls import path
from extras.views import ObjectChangeLogView

from . import views
from .models import *

app_name = 'nagios'
urlpatterns = [

    # Nagios checks
    path(r'nagios-checks/', views.NagiosCheckListView.as_view(), name='nagioscheck_list'),
    path(r'nagios-checks/add/', views.NagiosCheckCreateView.as_view(), name='nagioscheck_add'),
    path(r'nagios-checks/import/', views.NagiosCheckBulkImportView.as_view(), name='nagioscheck_import'),
    path(r'nagios-checks/delete/', views.NagiosCheckBulkDeleteView.as_view(), name='nagioscheck_bulk_delete'),
    path(r'nagios-checks/<int:pk>/edit/', views.NagiosCheckEditView.as_view(), name='nagioscheck_edit'),
    path(r'nagios-checks/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagioscheck_changelog', kwargs={'model': NagiosCheck}),
    
    # Nagios contacts
    path(r'nagios-contacts/', views.NagiosContactListView.as_view(), name='nagioscontact_list'),
    path(r'nagios-contacts/add/', views.NagiosContactCreateView.as_view(), name='nagioscontact_add'),
    path(r'nagios-contacts/import/', views.NagiosContactBulkImportView.as_view(), name='nagioscontact_import'),
    path(r'nagios-contacts/delete/', views.NagiosContactBulkDeleteView.as_view(), name='nagioscontact_bulk_delete'),
    path(r'nagios-contacts/<int:pk>/edit/', views.NagiosContactEditView.as_view(), name='nagioscontact_edit'),
    path(r'nagios-contacts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagioscontact_changelog', kwargs={'model': NagiosContact}),
    
    # Nagios contactgroups
    path(r'nagios-contactgroups/', views.NagiosContactGroupListView.as_view(), name='nagioscontactgroup_list'),
    path(r'nagios-contactgroups/add/', views.NagiosContactGroupCreateView.as_view(), name='nagioscontactgroup_add'),
    path(r'nagios-contactgroups/import/', views.NagiosContactGroupBulkImportView.as_view(), name='nagioscontactgroup_import'),
    path(r'nagios-contactgroups/delete/', views.NagiosContactGroupBulkDeleteView.as_view(), name='nagioscontactgroup_bulk_delete'),
    #path(r'nagios-contactgroups/<int:pk>/', views.NagiosContactGroupView.as_view(), name='nagioscontactgroup'),
    path(r'nagios-contactgroups/<int:pk>/edit/', views.NagiosContactGroupEditView.as_view(), name='nagioscontactgroup_edit'),
    path(r'nagios-contactgroups/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagioscontactgroup_changelog', kwargs={'model': NagiosContactGroup}),

    # Nagios hostgroups
    path(r'nagios-hostgroups/', views.NagiosHostGroupListView.as_view(), name='nagioshostgroup_list'),
    path(r'nagios-hostgroups/add/', views.NagiosHostGroupCreateView.as_view(), name='nagioshostgroup_add'),
    path(r'nagios-hostgroups/import/', views.NagiosHostGroupBulkImportView.as_view(), name='nagioshostgroup_import'),
    path(r'nagios-hostgroups/delete/', views.NagiosHostGroupBulkDeleteView.as_view(), name='nagioshostgroup_bulk_delete'),
    path(r'nagios-hostgroups/<int:pk>/edit/', views.NagiosHostGroupEditView.as_view(), name='nagioshostgroup_edit'),
    path(r'nagios-hostgroups/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagioshostgroup_changelog', kwargs={'model': NagiosHostGroup}),
    
    # Nagios hosttemplate
    path(r'nagios-hosttemplates/', views.NagiosHostTemplateListView.as_view(), name='nagioshosttemplate_list'),
    path(r'nagios-hosttemplates/add/', views.NagiosHostTemplateCreateView.as_view(), name='nagioshosttemplate_add'),
    path(r'nagios-hosttemplates/import/', views.NagiosHostTemplateBulkImportView.as_view(), name='nagioshosttemplate_import'),
    path(r'nagios-hosttemplates/delete/', views.NagiosHostTemplateBulkDeleteView.as_view(), name='nagioshosttemplate_bulk_delete'),
    path(r'nagios-hosttemplates/<int:pk>/edit/', views.NagiosHostTemplateEditView.as_view(), name='nagioshosttemplate_edit'),
    path(r'nagios-hosttemplates/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagioshosttemplate_changelog', kwargs={'model': NagiosHostTemplate}),
    
    # Nagios services
    path(r'nagios-services/', views.NagiosServiceListView.as_view(), name='nagiosservice_list'),
    path(r'nagios-services/add/', views.NagiosServiceCreateView.as_view(), name='nagiosservice_add'),
    path(r'nagios-services/import/', views.NagiosServiceBulkImportView.as_view(), name='nagiosservice_import'),
    path(r'nagios-services/delete/', views.NagiosServiceBulkDeleteView.as_view(), name='nagiosservice_bulk_delete'),
    path(r'nagios-services/<int:pk>/', views.NagiosServiceView.as_view(), name='nagiosservice'),
    path(r'nagios-services/<int:pk>/edit/', views.NagiosServiceEditView.as_view(), name='nagiosservice_edit'),
    path(r'nagios-services/<int:pk>/delete/', views.NagiosServiceDeleteView.as_view(), name='nagiosservice_delete'),
    path(r'nagios-services/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagiosservice_changelog', kwargs={'model': NagiosService}),

   # Nagios timeperiod
    path(r'nagios-timeperiods/', views.NagiosTimePeriodListView.as_view(), name='nagiostimeperiod_list'),
    path(r'nagios-timeperiods/add/', views.NagiosTimePeriodCreateView.as_view(), name='nagiostimeperiod_add'),
    path(r'nagios-timeperiods/import/', views.NagiosTimePeriodBulkImportView.as_view(), name='nagiostimeperiod_import'),
    path(r'nagios-timeperiods/delete/', views.NagiosTimePeriodBulkDeleteView.as_view(), name='nagiostimeperiod_bulk_delete'),
    path(r'nagios-timeperiods/<int:pk>/edit/', views.NagiosTimePeriodEditView.as_view(), name='nagiostimeperiod_edit'),
    path(r'nagios-timeperiods/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagiostimeperiod_changelog', kwargs={'model': NagiosTimePeriod}),

]
