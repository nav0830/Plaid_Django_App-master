# Generated by Django 3.2.7 on 2021-11-14 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solve', '0006_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 14, 15, 36, 10, 463335)),
        ),
    ]