# Generated by Django 4.0.6 on 2022-08-31 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0032_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(default=9989),
        ),
    ]
