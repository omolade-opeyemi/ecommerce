# Generated by Django 3.2.6 on 2021-12-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211206_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='name',
            new_name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
