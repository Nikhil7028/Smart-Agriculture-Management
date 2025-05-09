# Generated by Django 5.0.8 on 2025-04-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_officer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('titleimg', models.ImageField(upload_to='scheme_images/')),
                ('desc', models.TextField()),
                ('officialweb', models.URLField(blank=True, null=True)),
                ('ytVideo', models.URLField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
