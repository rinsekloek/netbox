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
    
    # Nagios services
    path(r'nagios-services/', views.NagiosServiceListView.as_view(), name='nagiosservice_list'),
    path(r'nagios-services/add/', views.NagiosServiceCreateView.as_view(), name='nagiosservice_add'),
    path(r'nagios-services/import/', views.NagiosServiceBulkImportView.as_view(), name='nagiosservice_import'),
    path(r'nagios-services/delete/', views.NagiosServiceBulkDeleteView.as_view(), name='nagiosservice_bulk_delete'),
    path(r'nagios-services/<int:pk>/', views.NagiosServiceView.as_view(), name='nagiosservice'),
    path(r'nagios-services/<int:pk>/edit/', views.NagiosServiceEditView.as_view(), name='nagiosservice_edit'),
    path(r'nagios-services/<int:pk>/delete/', views.NagiosServiceDeleteView.as_view(), name='nagiosservice_delete'),
    path(r'nagios-services/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagiosservice_changelog', kwargs={'model': NagiosService}),
    
    #path(r'nagios-services/device/<int:device>/add/', views.NagiosServiceCreateView.as_view(), name='device_nagiosservice_add'),

    # Nagios platform
    path(r'nagios-platforms/', views.NagiosPlatformListView.as_view(), name='nagiosplatform_list'),
    path(r'nagios-platforms/add/', views.NagiosPlatformCreateView.as_view(), name='nagiosplatform_add'),
    path(r'nagios-platforms/import/', views.NagiosPlatformBulkImportView.as_view(), name='nagiosplatform_import'),
    path(r'nagios-platforms/delete/', views.NagiosPlatformBulkDeleteView.as_view(), name='nagiosplatform_bulk_delete'),
    path(r'nagios-platforms/<int:pk>/edit/', views.NagiosPlatformEditView.as_view(), name='nagiosplatform_edit'),
    path(r'nagios-platforms/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nagiosplatform_changelog', kwargs={'model': NagiosPlatform}),

]
