# Generated by Django 4.0.2 on 2022-03-07 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0019_addplot_owner_addplot_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addplot',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='addplot',
            name='user_id',
        ),
    ]
