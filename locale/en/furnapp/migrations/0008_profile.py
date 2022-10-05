# Generated by Django 4.0.6 on 2022-08-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0007_remove_myuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='arrivals5.png', upload_to='profile')),
            ],
            options={
                'verbose_name': 'My Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]