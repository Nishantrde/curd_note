# Generated by Django 4.2.9 on 2024-02-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shadow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='first',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
