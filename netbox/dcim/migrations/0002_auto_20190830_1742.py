# Generated by Django 2.2.4 on 2019-08-30 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenancy', '0001_initial'),
        ('circuits', '0002_auto_20190830_1742'),
        ('dcim', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extras', '0002_auto_20190830_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualchassis',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='site',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='dcim.Region'),
        ),
        migrations.AddField(
            model_name='site',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='site',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sites', to='tenancy.Tenant'),
        ),
        migrations.AddField(
            model_name='region',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dcim.Region'),
        ),
        migrations.AddField(
            model_name='rearporttemplate',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rearport_templates', to='dcim.DeviceType'),
        ),
        migrations.AddField(
            model_name='rearport',
            name='cable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Cable'),
        ),
        migrations.AddField(
            model_name='rearport',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rearports', to='dcim.Device'),
        ),
        migrations.AddField(
            model_name='rearport',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='rackreservation',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='dcim.Rack'),
        ),
        migrations.AddField(
            model_name='rackreservation',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rackreservations', to='tenancy.Tenant'),
        ),
        migrations.AddField(
            model_name='rackreservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rackgroup',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rack_groups', to='dcim.Site'),
        ),
        migrations.AddField(
            model_name='rack',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racks', to='dcim.RackGroup'),
        ),
        migrations.AddField(
            model_name='rack',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='racks', to='dcim.RackRole'),
        ),
        migrations.AddField(
            model_name='rack',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='racks', to='dcim.Site'),
        ),
        migrations.AddField(
            model_name='rack',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='rack',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='racks', to='tenancy.Tenant'),
        ),
        migrations.AddField(
            model_name='powerporttemplate',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='powerport_templates', to='dcim.DeviceType'),
        ),
        migrations.AddField(
            model_name='powerport',
            name='_connected_powerfeed',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.PowerFeed'),
        ),
        migrations.AddField(
            model_name='powerport',
            name='_connected_poweroutlet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='connected_endpoint', to='dcim.PowerOutlet'),
        ),
        migrations.AddField(
            model_name='powerport',
            name='cable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Cable'),
        ),
        migrations.AddField(
            model_name='powerport',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='powerports', to='dcim.Device'),
        ),
        migrations.AddField(
            model_name='powerport',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='powerpanel',
            name='rack_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dcim.RackGroup'),
        ),
        migrations.AddField(
            model_name='powerpanel',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dcim.Site'),
        ),
        migrations.AddField(
            model_name='poweroutlettemplate',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poweroutlet_templates', to='dcim.DeviceType'),
        ),
        migrations.AddField(
            model_name='poweroutlettemplate',
            name='power_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poweroutlet_templates', to='dcim.PowerPortTemplate'),
        ),
        migrations.AddField(
            model_name='poweroutlet',
            name='cable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Cable'),
        ),
        migrations.AddField(
            model_name='poweroutlet',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poweroutlets', to='dcim.Device'),
        ),
        migrations.AddField(
            model_name='poweroutlet',
            name='power_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poweroutlets', to='dcim.PowerPort'),
        ),
        migrations.AddField(
            model_name='poweroutlet',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='powerfeed',
            name='cable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Cable'),
        ),
        migrations.AddField(
            model_name='powerfeed',
            name='connected_endpoint',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.PowerPort'),
        ),
        migrations.AddField(
            model_name='powerfeed',
            name='power_panel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='powerfeeds', to='dcim.PowerPanel'),
        ),
        migrations.AddField(
            model_name='powerfeed',
            name='rack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dcim.Rack'),
        ),
        migrations.AddField(
            model_name='powerfeed',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='platform',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='platforms', to='dcim.Manufacturer'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='dcim.Device'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='inventory_items', to='dcim.Manufacturer'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_items', to='dcim.InventoryItem'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='interfacetemplate',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interface_templates', to='dcim.DeviceType'),
        ),
        migrations.AddField(
            model_name='interface',
            name='_connected_circuittermination',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='circuits.CircuitTermination'),
        ),
        migrations.AddField(
            model_name='interface',
            name='_connected_interface',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Interface'),
        ),
        migrations.AddField(
            model_name='interface',
            name='cable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Cable'),
        ),
        migrations.AddField(
            model_name='interface',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='dcim.Device'),
        ),
        migrations.AddField(
            model_name='interface',
            name='lag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_interfaces', to='dcim.Interface'),
        ),
    ]