# Generated by Django 4.2.4 on 2024-03-16 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0064_cart_design'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_design',
            name='work_design',
        ),
    ]
