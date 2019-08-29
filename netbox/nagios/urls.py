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

]
