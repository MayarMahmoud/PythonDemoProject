# Generated by Django 3.2.13 on 2022-06-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.CharField(default=1234, max_length=32, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]