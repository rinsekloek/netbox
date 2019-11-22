# Generated by Django 2.2.4 on 2019-08-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenancy', '0001_initial'),
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configcontext',
            name='tenant_groups',
            field=models.ManyToManyField(blank=True, related_name='_configcontext_tenant_groups_+', to='tenancy.TenantGroup'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='tenants',
            field=models.ManyToManyField(blank=True, related_name='_configcontext_tenants_+', to='tenancy.Tenant'),
        ),
        migrations.AlterUniqueTogether(
            name='webhook',
            unique_together={('payload_url', 'type_create', 'type_update', 'type_delete')},
        ),
        migrations.AlterIndexTogether(
            name='taggeditem',
            index_together={('content_type', 'object_id')},
        ),
        migrations.AlterUniqueTogether(
            name='exporttemplate',
            unique_together={('content_type', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='customfieldvalue',
            unique_together={('field', 'obj_type', 'obj_id')},
        ),
        migrations.AlterUniqueTogether(
            name='customfieldchoice',
            unique_together={('field', 'value')},
        ),
    ]