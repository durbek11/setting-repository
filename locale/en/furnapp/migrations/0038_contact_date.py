# Generated by Django 4.1 on 2022-09-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0037_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]