# Generated by Django 5.0.2 on 2024-05-31 05:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0082_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6b5409b1-6bcc-43ef-a023-93b9330a077e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
