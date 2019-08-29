import django_tables2 as tables
from django_tables2.utils import Accessor

from dcim.models import *
from utilities.tables import BaseTable, ToggleColumn
from .models import *

NAGIOSCHECK_ACTIONS = """
<a href="{% url 'nagios:nagioscheck_changelog' pk=record.pk %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.nagios.change_nagioscheck %}
    <a href="{% url 'nagios:nagioscheck_edit'  pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

NAGIOSCONTACT_ACTIONS = """
<a href="{% url 'nagios:nagioscontact_changelog' pk=record.pk %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.nagios.change_nagioscontact %}
    <a href="{% url 'nagios:nagioscontact_edit'  pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

#
# Nagios checks
#

class NagiosCheckTable(BaseTable):
    pk = ToggleColumn()
    actions = tables.TemplateColumn(
        template_code=NAGIOSCHECK_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosCheck
        fields = ('pk','check_name', 'check_command')

        
class NagiosContactTable(BaseTable):
    pk = ToggleColumn()
    
    actions = tables.TemplateColumn(
        template_code=NAGIOSCONTACT_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosContact
        fields = ('pk', 'alias', 'email','pager', 'service_notification_period', 'host_notification_period', 'service_notification_options')



