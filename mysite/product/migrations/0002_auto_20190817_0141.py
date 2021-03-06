# Generated by Django 2.2.3 on 2019-08-16 22:41

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[(0, 'False'), (1, 'True')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[(2, 'L'), (3, 'XL'), (1, 'M'), (36, '36 Beden'), (34, '34 Beden'), (0, 'XS'), (40, '40 Beden')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(0, 'False'), (1, 'True')]),
        ),
    ]
