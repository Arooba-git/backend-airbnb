# Generated by Django 5.0.6 on 2024-05-16 09:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0029_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c8da1389-22ef-4779-9756-a15c9f1b6731'), editable=False, primary_key=True, serialize=False),
        ),
    ]
