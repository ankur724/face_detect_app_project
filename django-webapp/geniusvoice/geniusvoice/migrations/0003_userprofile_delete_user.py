# Generated by Django 4.2.6 on 2023-10-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geniusvoice', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]