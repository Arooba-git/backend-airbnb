# Generated by Django 5.0.2 on 2024-05-21 02:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0058_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9a2f1c27-7e83-4b46-a5b3-1f2f73b4f6f8'), editable=False, primary_key=True, serialize=False),
        ),
    ]
