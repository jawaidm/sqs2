# Generated by Django 3.2.4 on 2023-03-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqs', '0008_rename_layeraccesslog_layerrequestlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerrequestlog',
            name='when',
            field=models.DateTimeField(),
        ),
    ]