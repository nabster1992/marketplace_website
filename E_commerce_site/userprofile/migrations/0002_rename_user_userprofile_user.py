# Generated by Django 4.2.3 on 2023-07-30 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='User',
            new_name='user',
        ),
    ]