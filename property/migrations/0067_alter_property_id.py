# Generated by Django 5.0.2 on 2024-05-22 06:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0066_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a69e5f20-f82a-4538-9821-505fa6ffbd81'), editable=False, primary_key=True, serialize=False),
        ),
    ]
