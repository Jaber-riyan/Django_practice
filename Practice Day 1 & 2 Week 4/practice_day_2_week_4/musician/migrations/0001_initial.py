# Generated by Django 4.2.7 on 2023-12-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=12)),
                ('instrument_type', models.CharField(max_length=50)),
            ],
        ),
    ]
