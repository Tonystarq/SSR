# Generated by Django 4.0.2 on 2022-03-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0002_customer_addresss_customer_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='addresss',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]