# Generated by Django 2.2.3 on 2019-08-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20190822_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[(1, 'True'), (0, 'False')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[(36, '36 Beden'), (3, 'XL'), (40, '40 Beden'), (1, 'M'), (2, 'L'), (34, '34 Beden'), (0, 'XS')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'True'), (0, 'False')]),
        ),
    ]