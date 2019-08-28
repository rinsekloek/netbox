import django_tables2 as tables
from django_tables2.utils import Accessor

from dcim.models import *
from utilities.tables import BaseTable, ToggleColumn
from .models import *

NAGIOSCHECK_ACTIONS = """
{% if perms.nagios.change_nagioscheck %}
    <a href="{% url 'nagios:nagioscheck_edit'  %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""


#
# Nagios checks
#

class NagiosCheckTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    nagioscheck_count = tables.Column(verbose_name='NagiosCheck')
    actions = tables.TemplateColumn(
        template_code=NAGIOSCHECK_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosCheck
        fields = ('check_name', 'check_command')


