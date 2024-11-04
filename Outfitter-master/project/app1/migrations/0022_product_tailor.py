# Generated by Django 4.2.5 on 2023-11-03 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_measurement_color_measurement_fabric_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tailor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tailored_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
