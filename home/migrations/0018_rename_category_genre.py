# Generated by Django 3.2.6 on 2021-12-17 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_product_cat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Genre',
        ),
    ]
