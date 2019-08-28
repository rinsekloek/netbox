from django.urls import path
from extras.views import ObjectChangeLogView

from . import views
from .models import NagiosCheck

app_name = 'nagios'
urlpatterns = [

    # Secret roles
    path(r'nagios-checks/', views.NagiosCheckListView.as_view(), name='nagioscheck_list'),
    path(r'nagios-checks/add/', views.NagiosCheckCreateView.as_view(), name='nagioscheck_add'),
    path(r'nagios-checks/import/', views.NagiosCheckBulkImportView.as_view(), name='nagioscheck_import'),
    path(r'nagios-checks/delete/', views.NagiosCheckBulkDeleteView.as_view(), name='nagioscheck_bulk_delete'),
    #path(r'nagios-checks/<int:pk>/edit/', views.NagiosCheckEditView.as_view(), name='nagioscheck_edit'),
    path(r'nagios-checks/edit/', views.NagiosCheckEditView.as_view(), name='nagioscheck_edit'),

]
