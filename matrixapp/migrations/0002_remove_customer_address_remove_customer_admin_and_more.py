# Generated by Django 4.0.2 on 2022-02-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='bookplot',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='receipt/'),
        ),
    ]