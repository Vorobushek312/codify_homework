# Generated by Django 3.2.7 on 2021-10-24 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='allow_mailling',
            new_name='allow_mailing',
        ),
    ]
