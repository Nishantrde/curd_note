# Generated by Django 4.2.10 on 2024-03-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0014_alter_user_class_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_class',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='user_id',
        ),
        migrations.AddField(
            model_name='notes',
            name='profile_name',
            field=models.CharField(default='', max_length=55),
        ),
    ]
