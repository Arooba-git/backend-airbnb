# Generated by Django 5.0.2 on 2024-05-31 04:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0080_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b26a04eb-2105-48b7-ad2a-84c70ba67a29'), editable=False, primary_key=True, serialize=False),
        ),
    ]
