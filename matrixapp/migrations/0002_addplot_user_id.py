# Generated by Django 4.0.2 on 2022-02-28 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addplot',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
