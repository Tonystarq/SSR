# Generated by Django 4.0.2 on 2022-03-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0017_funddetails_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='funddetails',
            name='joinig_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
