# Generated by Django 5.0.8 on 2025-04-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0004_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='mobno',
            field=models.CharField(default=1234567890, max_length=10),
            preserve_default=False,
        ),
    ]
