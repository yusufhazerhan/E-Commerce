# Generated by Django 2.2.3 on 2019-08-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20190822_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[(3, 'XL'), (34, '34 Beden'), (0, 'XS'), (1, 'M'), (2, 'L'), (40, '40 Beden'), (36, '36 Beden')]),
        ),
    ]
