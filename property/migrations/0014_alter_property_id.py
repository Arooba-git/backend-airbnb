# Generated by Django 5.0.6 on 2024-05-16 06:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('86e61453-75ff-415a-81b6-edebbf72da4e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
