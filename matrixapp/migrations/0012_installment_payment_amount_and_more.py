# Generated by Django 4.0.2 on 2022-03-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0011_installment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='installment',
            name='payment_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='installment',
            name='remaining_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]