# Generated by Django 4.0.6 on 2022-08-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0019_profile_address_profile_hobbies_profile_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='card_number',
            field=models.CharField(blank=True, max_length=21),
        ),
    ]
