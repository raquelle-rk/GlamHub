# Generated by Django 3.0.8 on 2020-08-18 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='portfolio',
        ),
    ]
