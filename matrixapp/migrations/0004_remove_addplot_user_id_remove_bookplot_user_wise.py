# Generated by Django 4.0.2 on 2022-02-28 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0003_bookplot_user_wise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addplot',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='bookplot',
            name='user_wise',
        ),
    ]