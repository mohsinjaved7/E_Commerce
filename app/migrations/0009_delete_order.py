# Generated by Django 4.2.4 on 2023-08-23 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_order_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
