# Generated by Django 4.0.2 on 2022-03-05 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0009_bookplot_remaining_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installment',
            name='father_name',
        ),
    ]
