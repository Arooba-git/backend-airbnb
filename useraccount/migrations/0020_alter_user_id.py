# Generated by Django 5.0.6 on 2024-05-16 06:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0019_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f6a6c51c-f799-4d57-a945-4acff2c56d08'), editable=False, primary_key=True, serialize=False),
        ),
    ]
