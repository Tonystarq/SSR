# Generated by Django 4.0.2 on 2022-03-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0007_installment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookplot',
            name='booking_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
