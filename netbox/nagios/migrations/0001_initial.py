# Generated by Django 2.2.4 on 2019-08-30 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NagiosCheck',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('check_name', models.CharField(max_length=255)),
                ('check_command', models.CharField(max_length=512)),
                ('performance_value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'nagios_checks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosContactGroup',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('alias', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'nagios_contactgroups',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosPlatforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'nagios_platforms',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosTimeperiods',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('alias', models.CharField(max_length=255)),
                ('timespan', models.TextField()),
            ],
            options={
                'db_table': 'nagios_timeperiods',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosService',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('use_template', models.IntegerField(blank=True, null=True)),
                ('service_description', models.CharField(max_length=255)),
                ('active_checks_enabled', models.SmallIntegerField(blank=True, null=True)),
                ('passive_checks_enabled', models.SmallIntegerField(blank=True, null=True)),
                ('check_command_params', models.CharField(max_length=255)),
                ('max_check_attempts', models.IntegerField(blank=True, null=True)),
                ('normal_check_interval', models.IntegerField(blank=True, null=True)),
                ('retry_check_interval', models.IntegerField(blank=True, null=True)),
                ('notification_interval', models.SmallIntegerField(blank=True, null=True)),
                ('notification_options', models.CharField(blank=True, max_length=64, null=True)),
                ('notifications_enabled', models.SmallIntegerField(blank=True, null=True)),
                ('event_handler', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_groups', models.TextField(blank=True, null=True)),
                ('check_command', models.ForeignKey(db_column='check_command', on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosCheck')),
                ('check_period', models.ForeignKey(db_column='check_period', on_delete=django.db.models.deletion.DO_NOTHING, related_name='check_period', to='nagios.NagiosTimeperiods')),
                ('notification_period', models.ForeignKey(blank=True, db_column='notification_period', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='notification_period', to='nagios.NagiosTimeperiods')),
                ('server', models.ForeignKey(blank=True, db_column='server', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='server', to='dcim.Device')),
            ],
            options={
                'db_table': 'nagios_services',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosServers',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('naam', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=64)),
                ('pass_field', models.CharField(db_column='pass', max_length=64)),
                ('configpath_remote', models.CharField(max_length=255)),
                ('configpath_local', models.CharField(max_length=255)),
                ('initscript', models.CharField(max_length=255)),
                ('platform', models.ForeignKey(blank=True, db_column='platform', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosPlatforms')),
            ],
            options={
                'db_table': 'nagios_servers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosHosttemplates',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('use_template', models.IntegerField(blank=True, null=True)),
                ('max_check_attempts', models.SmallIntegerField(blank=True, null=True)),
                ('notification_interval', models.SmallIntegerField(blank=True, null=True)),
                ('notification_options', models.CharField(blank=True, max_length=64, null=True)),
                ('notifications_enabled', models.SmallIntegerField(blank=True, null=True)),
                ('check_command', models.ForeignKey(blank=True, db_column='check_command', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosCheck')),
                ('notification_period', models.ForeignKey(blank=True, db_column='notification_period', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosTimeperiods')),
            ],
            options={
                'db_table': 'nagios_hosttemplates',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosHostGroup',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('alias', models.CharField(max_length=255)),
                ('platform', models.ForeignKey(blank=True, db_column='platform', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosPlatforms')),
            ],
            options={
                'db_table': 'nagios_hostgroups',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosContact',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=255)),
                ('service_notification_options', models.CharField(max_length=64)),
                ('host_notification_options', models.CharField(max_length=64)),
                ('service_notification_commands', models.CharField(max_length=255)),
                ('host_notification_commands', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('pager', models.CharField(max_length=255)),
                ('contactgroups', models.ManyToManyField(to='nagios.NagiosContactGroup')),
                ('host_notification_period', models.ForeignKey(db_column='host_notification_period', on_delete=django.db.models.deletion.DO_NOTHING, related_name='host_notification_period', to='nagios.NagiosTimeperiods')),
                ('service_notification_period', models.ForeignKey(db_column='service_notification_period', on_delete=django.db.models.deletion.DO_NOTHING, related_name='service_notification_period', to='nagios.NagiosTimeperiods')),
            ],
            options={
                'db_table': 'nagios_contacts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NagiosServicesContactgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('contactgroup', models.ForeignKey(blank=True, db_column='contactgroup', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosContactGroup')),
                ('service', models.ForeignKey(blank=True, db_column='service', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosService')),
            ],
            options={
                'db_table': 'nagios_services_contactgroups',
                'managed': True,
                'unique_together': {('service', 'contactgroup')},
            },
        ),
    ]
