# Generated by Django 4.1.3 on 2023-03-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
