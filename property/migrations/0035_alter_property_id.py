# Generated by Django 5.0.6 on 2024-05-17 02:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0034_alter_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9af02af4-5bcf-42d4-862c-654b062f34fa'), editable=False, primary_key=True, serialize=False),
        ),
    ]
