# Generated by Django 2.2.3 on 2019-08-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20190827_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Refused', 'Refused'), ('OnShipping', 'OnShipping'), ('Preparing', 'Preparing'), ('NEW', 'New')], default='New', max_length=15),
        ),
    ]