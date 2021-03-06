# Generated by Django 3.2.7 on 2021-11-14 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solve', '0004_alter_transaction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='mask',
        ),
        migrations.RemoveField(
            model_name='account',
            name='subtype',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='account_owner',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='authorized_date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='category',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='iso_currency_code',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='location',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='merchant_name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_channel',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_meta',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='pending_transaction_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_code',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='unofficial_currency_code',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 14, 14, 57, 6, 586847)),
        ),
    ]
