# Generated by Django 3.2.6 on 2021-12-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211207_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
