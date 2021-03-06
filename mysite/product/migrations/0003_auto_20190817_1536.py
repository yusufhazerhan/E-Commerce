# Generated by Django 2.2.3 on 2019-08-17 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190817_0141'),
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
            field=models.IntegerField(choices=[(34, '34 Beden'), (2, 'L'), (3, 'XL'), (36, '36 Beden'), (0, 'XS'), (40, '40 Beden'), (1, 'M')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'True'), (0, 'False')]),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
