# Generated by Django 3.2 on 2021-05-06 08:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20210506_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='houseNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='fejl', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='postalCode',
            field=models.IntegerField(),
        ),
    ]
