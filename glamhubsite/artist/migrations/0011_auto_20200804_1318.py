# Generated by Django 3.0.8 on 2020-08-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0010_auto_20200804_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistportfolio',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
