# Generated by Django 4.2.9 on 2024-01-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms18', '0021_requisition_req_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='awaiting_approval',
            field=models.BooleanField(default=False),
        ),
    ]
