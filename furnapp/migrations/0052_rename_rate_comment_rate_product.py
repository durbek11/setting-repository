# Generated by Django 4.0.6 on 2022-09-21 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0051_comment_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='rate',
            new_name='rate_product',
        ),
    ]
