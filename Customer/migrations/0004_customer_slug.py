# Generated by Django 4.1.5 on 2023-03-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default=' ', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
