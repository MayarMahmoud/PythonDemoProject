# Generated by Django 3.2.13 on 2022-06-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to='website/static/product/images/'),
        ),
    ]