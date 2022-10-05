# Generated by Django 4.0.6 on 2022-08-31 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0031_remove_profile_facebook_remove_profile_github_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('choices', models.CharField(choices=[('Taklif', 'Taklif'), ('Shikoyat', 'Shikoyat')], default='Taklif', max_length=8)),
                ('mobile', models.IntegerField(default='+9989')),
            ],
        ),
    ]