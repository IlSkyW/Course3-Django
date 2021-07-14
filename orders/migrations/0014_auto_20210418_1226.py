# Generated by Django 3.2 on 2021-04-18 09:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20210418_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(help_text='Example: +380663846078 / 0663846078', max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(help_text='Example: 20501, 30512', max_length=5, validators=[django.core.validators.RegexValidator(regex='^ (^[0-9]{5}(?:-[0-9]{4})?$ | ^ $)')]),
        ),
    ]
