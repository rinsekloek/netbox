# Generated by Django 2.2.4 on 2019-09-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagios', '0006_auto_20190831_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nagiosservice',
            name='active_checks_enabled',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nagiosservice',
            name='passive_checks_enabled',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]