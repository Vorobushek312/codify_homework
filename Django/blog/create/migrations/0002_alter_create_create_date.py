# Generated by Django 3.2.7 on 2021-10-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]