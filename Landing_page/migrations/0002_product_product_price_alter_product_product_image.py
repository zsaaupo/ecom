# Generated by Django 4.1.5 on 2023-03-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default='  ', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product/image'),
        ),
    ]