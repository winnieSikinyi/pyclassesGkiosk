# Generated by Django 4.2.3 on 2023-08-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
