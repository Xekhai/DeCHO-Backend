# Generated by Django 4.0.1 on 2022-03-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_change_default_for_photo_url_column'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giveaway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
