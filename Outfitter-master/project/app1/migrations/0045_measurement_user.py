# Generated by Django 4.2.5 on 2023-11-22 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0044_alter_order_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
