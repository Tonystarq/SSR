# Generated by Django 4.0.2 on 2022-03-06 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0013_rename_booking_amount_bookplot_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installment',
            name='payment_amount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
