# Generated by Django 4.2.10 on 2024-03-15 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_alter_userprofile_user_prop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_prop',
            new_name='user',
        ),
    ]