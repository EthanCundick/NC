# Generated by Django 3.1.5 on 2021-01-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210125_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='about_text_one',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='about_text_two',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
