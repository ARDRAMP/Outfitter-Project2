# Generated by Django 4.2.5 on 2023-11-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_measurement_sleev_design'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='additional_info',
            field=models.TextField(blank=True, help_text='Add any additional information here.', null=True, verbose_name='Additional Information'),
        ),
    ]
