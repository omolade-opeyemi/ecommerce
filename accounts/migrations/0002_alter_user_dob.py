# Generated by Django 3.2.6 on 2021-12-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
