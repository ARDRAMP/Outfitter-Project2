# Generated by Django 4.2.5 on 2024-02-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0053_thread_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
