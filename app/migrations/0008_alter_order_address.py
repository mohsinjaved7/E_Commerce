# Generated by Django 4.2.4 on 2023-08-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_order_phone_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(max_length=100),
        ),
    ]
