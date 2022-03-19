# Generated by Django 3.2.11 on 2022-03-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
