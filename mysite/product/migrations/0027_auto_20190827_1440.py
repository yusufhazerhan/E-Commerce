# Generated by Django 2.2.3 on 2019-08-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20190827_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[(1, 'M'), (3, 'XL'), (2, 'L'), (0, 'XS'), (34, '34 Beden'), (40, '40 Beden'), (36, '36 Beden')]),
        ),
    ]