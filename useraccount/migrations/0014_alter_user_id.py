# Generated by Django 5.0.6 on 2024-05-16 06:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0013_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1ac39bd8-9601-43f9-a1ae-f5b93aa7de1b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
