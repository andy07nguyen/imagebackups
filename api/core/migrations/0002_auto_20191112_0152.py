# Generated by Django 2.2.7 on 2019-11-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupjob',
            name='started',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
