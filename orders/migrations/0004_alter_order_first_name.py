# Generated by Django 3.2 on 2021-04-17 07:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]+$')], verbose_name='name'),
        ),
    ]
