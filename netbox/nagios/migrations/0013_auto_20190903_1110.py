# Generated by Django 2.2.4 on 2019-09-03 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nagios', '0012_nagiosplatform_platform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nagiosservers',
            name='platform',
        ),
        migrations.AlterField(
            model_name='nagioshostgroup',
            name='platform',
            field=models.ForeignKey(blank=True, db_column='platform', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nagioshostgroup', to='dcim.Platform'),
        ),
        migrations.DeleteModel(
            name='NagiosPlatform',
        ),
        migrations.DeleteModel(
            name='NagiosServers',
        ),
    ]
