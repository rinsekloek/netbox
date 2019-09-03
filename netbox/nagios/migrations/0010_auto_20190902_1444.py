# Generated by Django 2.2.4 on 2019-09-02 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nagios', '0009_auto_20190901_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nagiosservice',
            name='check_command',
            field=models.ForeignKey(blank=True, db_column='check_command', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nagios.NagiosCheck'),
        ),
        migrations.AlterField(
            model_name='nagiosservice',
            name='check_command_params',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='nagiosservice',
            name='check_period',
            field=models.ForeignKey(blank=True, db_column='check_period', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='check_period', to='nagios.NagiosTimeperiods'),
        ),
        migrations.AlterField(
            model_name='nagiosservice',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
