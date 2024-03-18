# Generated by Django 4.2.10 on 2024-03-03 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shadow', '0005_remove_first_address_remove_first_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Second',
            fields=[
                ('first_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shadow.first')),
                ('address', models.CharField(max_length=100)),
                ('i_d', models.IntegerField()),
            ],
            bases=('shadow.first',),
        ),
    ]