# Generated by Django 2.2.3 on 2019-08-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20190824_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[(36, '36 Beden'), (40, '40 Beden'), (2, 'L'), (3, 'XL'), (0, 'XS'), (34, '34 Beden'), (1, 'M')]),
        ),
    ]
