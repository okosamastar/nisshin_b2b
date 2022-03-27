# Generated by Django 3.2.11 on 2022-03-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_category_the_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['the_order']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['the_order']},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['the_order']},
        ),
        migrations.AlterModelOptions(
            name='industry',
            options={'ordering': ['the_order']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['the_order']},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['the_order']},
        ),
        migrations.AddField(
            model_name='brand',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='facility',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='industry',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='series',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]