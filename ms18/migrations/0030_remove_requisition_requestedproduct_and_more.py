# Generated by Django 5.0.1 on 2024-01-15 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms18', '0029_remove_requisition_requested_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='requestedproduct',
        ),
        migrations.AddField(
            model_name='requestedproduct',
            name='Requisition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ms18.requisition'),
        ),
    ]
