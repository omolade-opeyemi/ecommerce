# Generated by Django 3.2.6 on 2021-12-17 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
