# Generated by Django 4.2.4 on 2023-08-21 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecommerce/pimg')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sub_category')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
