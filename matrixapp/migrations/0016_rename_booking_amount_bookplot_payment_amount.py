# Generated by Django 4.0.2 on 2022-03-06 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0015_rename_payment_amount_bookplot_booking_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookplot',
            old_name='booking_amount',
            new_name='payment_amount',
        ),
    ]
