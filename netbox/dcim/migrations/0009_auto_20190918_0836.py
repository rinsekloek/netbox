# Generated by Django 2.2.4 on 2019-09-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0008_device_nagios_parents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='nagios_parents',
            field=models.ManyToManyField(related_name='_device_nagios_parents_+', to='dcim.Device'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
