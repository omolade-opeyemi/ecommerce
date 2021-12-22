# Generated by Django 3.2.6 on 2021-12-21 16:18

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_product_prod_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=100, size=[160, 160], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=100, size=[500, 375], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=100, size=[500, 375], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=100, size=[500, 375], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=100, size=[500, 375], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img6',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=100, size=[500, 375], upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img7',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=100, size=[500, 375], upload_to=''),
        ),
    ]