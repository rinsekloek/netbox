# Generated by Django 2.2.4 on 2019-08-30 17:42

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0001_initial'),
        ('tenancy', '0001_initial'),
        ('circuits', '0001_initial'),
        ('dcim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='circuittermination',
            name='cable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Cable'),
        ),
        migrations.AddField(
            model_name='circuittermination',
            name='circuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terminations', to='circuits.Circuit'),
        ),
        migrations.AddField(
            model_name='circuittermination',
            name='connected_endpoint',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.Interface'),
        ),
        migrations.AddField(
            model_name='circuittermination',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='circuit_terminations', to='dcim.Site'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='circuits', to='circuits.Provider'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='circuits', to='tenancy.Tenant'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='circuits', to='circuits.CircuitType'),
        ),
        migrations.AlterUniqueTogether(
            name='circuittermination',
            unique_together={('circuit', 'term_side')},
        ),
        migrations.AlterUniqueTogether(
            name='circuit',
            unique_together={('provider', 'cid')},
        ),
    ]
