# Generated by Django 2.2.4 on 2019-08-31 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagios', '0005_auto_20190830_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nagiosservice',
            name='active_checks_enabled',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nagiosservice',
            name='passive_checks_enabled',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
