# Generated by Django 2.2.3 on 2019-08-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20190823_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[(0, 'False'), (1, 'True')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[(3, 'XL'), (2, 'L'), (36, '36 Beden'), (0, 'XS'), (1, 'M'), (34, '34 Beden'), (40, '40 Beden')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(0, 'False'), (1, 'True')]),
        ),
    ]
