# Generated by Django 3.2.6 on 2021-12-21 15:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_product_twenty_percent_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[160, 160], upload_to=''),
        ),
    ]