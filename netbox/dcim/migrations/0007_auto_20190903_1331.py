# Generated by Django 2.2.4 on 2019-09-03 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nagios', '0013_auto_20190903_1110'),
        ('dcim', '0006_remove_device_observium_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='nagios_contactgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='nagios.NagiosContactGroup'),
        ),
        migrations.AddField(
            model_name='device',
            name='nagios_hostgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='nagios.NagiosHostGroup'),
        ),
        migrations.AddField(
            model_name='device',
            name='nagios_hosttemplate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='nagios.NagiosHostTemplate'),
        ),
    ]