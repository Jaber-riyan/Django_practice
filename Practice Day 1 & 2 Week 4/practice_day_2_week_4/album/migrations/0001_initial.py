# Generated by Django 4.2.7 on 2023-12-07 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('album_release_date', models.DateTimeField(default=datetime.datetime(2023, 12, 7, 17, 20, 32, 982507))),
                ('rating', models.CharField(choices=[('2', '2'), ('3', '3'), ('1', '1'), ('4', '4'), ('5', '5')], max_length=100)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musicianmodel')),
            ],
        ),
    ]
