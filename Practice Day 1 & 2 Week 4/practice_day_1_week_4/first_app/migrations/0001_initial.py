# Generated by Django 4.2.7 on 2023-12-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=200)),
                ('rating', models.CharField(choices=[('1', '1'), ('3', '3'), ('2', '2')], max_length=10)),
            ],
        ),
    ]
