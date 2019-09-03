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

NAGIOSSERVICE_ACTIONS = """
<a href="{% url 'nagios:nagiosservice_changelog' pk=record.pk %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.nagios.change_nagiosservice %}
    <a href="{% url 'nagios:nagiosservice_edit'  pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

NAGIOSCONTACTGROUP_ACTIONS = """
<a href="{% url 'nagios:nagioscontactgroup_changelog' pk=record.pk %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.nagios.change_nagioscontactgroup %}
    <a href="{% url 'nagios:nagioscontactgroup_edit'  pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

NAGIOSHOSTGROUP_ACTIONS = """
<a href="{% url 'nagios:nagioshostgroup_changelog' pk=record.pk %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.nagios.change_nagioshostgroup %}
    <a href="{% url 'nagios:nagioshostgroup_edit'  pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

NAGIOSHOSTTEMPLATE_ACTIONS = """
<a href="{% url 'nagios:nagioshosttemplate_changelog' pk=record.pk %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.nagios.change_nagioshosttemplate %}
    <a href="{% url 'nagios:nagioshosttemplate_edit'  pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""


NAGIOSTIMEPERIOD_ACTIONS = """
<a href="{% url 'nagios:nagiostimeperiod_changelog' pk=record.pk %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.nagios.change_nagiostimeperiod %}
    <a href="{% url 'nagios:nagiostimeperiod_edit'  pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

PLATFORM_DEVICES = """
<a href="{% url 'dcim:device_list' %}?id={{ record.platform.pk }}">{{ value }}</a>
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


class NagiosContactGroupTable(BaseTable):
    pk = ToggleColumn()
    
    
    actions = tables.TemplateColumn(
        template_code=NAGIOSCONTACTGROUP_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosContactGroup
        fields = ('pk', 'name', 'alias','contacts')

class NagiosHostGroupTable(BaseTable):
    pk = ToggleColumn()
    
    #platform = tables.LinkColumn(
    #    viewname='dcim:platform_edit',
    #    args=[Accessor('dcim.slug')]
    #)
    platform = tables.TemplateColumn(
        template_code=PLATFORM_DEVICES,
        attrs={'slug': 'dcim.platform.slug'},
        orderable=False,
        verbose_name='Platform devices'
    )
    
    actions = tables.TemplateColumn(
        template_code=NAGIOSHOSTGROUP_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosHostGroup
        fields = ('pk', 'name', 'alias','platform')

        
class NagiosHostTemplateTable(BaseTable):
    pk = ToggleColumn()
    
    #use_template = tables.LinkColumn('nagioshosttemplate_edit', args=[Accessor('pk')])
        
    actions = tables.TemplateColumn(
        template_code=NAGIOSHOSTTEMPLATE_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosHostTemplate
        fields = ('pk', 'name', 'use_template', 'check_command', 'max_check_attempts', 'notification_interval', 'notification_period', 'notification_options', 'notifications_enabled')

         
class NagiosServiceTable(BaseTable):
    pk = ToggleColumn()
    use_template = tables.LinkColumn(
        viewname='nagios:nagiosservice_edit',
        args=[Accessor('pk')]
    )
    
    device = tables.LinkColumn(
        viewname='dcim:device',
        args=[Accessor('device.pk')]
    )
    
    actions = tables.TemplateColumn(
        template_code=NAGIOSSERVICE_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosService
        fields = ('pk', 'name', 'use_template', 'device', 'service_description','contact_groups')

        
class NagiosTimePeriodTable(BaseTable):
    pk = ToggleColumn()
    
    actions = tables.TemplateColumn(
        template_code=NAGIOSTIMEPERIOD_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = NagiosTimePeriod
        fields = ('pk', 'name', 'alias', 'timespan')



