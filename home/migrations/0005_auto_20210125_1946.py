# Generated by Django 3.1.5 on 2021-01-25 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
