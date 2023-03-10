# Generated by Django 4.1.5 on 2023-03-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing_page', '0004_alter_order_kg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_charge',
            new_name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_charge',
            field=models.PositiveIntegerField(default='2'),
            preserve_default=False,
        ),
    ]
