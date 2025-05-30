# Generated by Django 5.0.8 on 2025-04-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('mobno', models.CharField(max_length=10)),
                ('whatappsno', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=90)),
                ('village', models.CharField(max_length=90)),
                ('dist', models.CharField(max_length=90)),
                ('subdist', models.CharField(max_length=90)),
                ('pincode', models.IntegerField(max_length=90)),
                ('totalland', models.IntegerField()),
                ('maincrop', models.CharField(max_length=90)),
                ('irrigation', models.CharField(max_length=90)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
