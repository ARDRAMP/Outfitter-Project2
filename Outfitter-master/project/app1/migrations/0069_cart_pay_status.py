# Generated by Django 4.2.5 on 2024-04-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0068_payment2'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pay_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
