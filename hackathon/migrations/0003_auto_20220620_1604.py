# Generated by Django 3.2.13 on 2022-06-20 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_auto_20220620_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='stock_code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='stock_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.companies'),
        ),
    ]
