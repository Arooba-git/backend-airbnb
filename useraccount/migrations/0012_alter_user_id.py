# Generated by Django 5.0.6 on 2024-05-16 05:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0011_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3db66549-895e-4194-acd0-fbdca84b8214'), editable=False, primary_key=True, serialize=False),
        ),
    ]
