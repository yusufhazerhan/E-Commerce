# Generated by Django 2.2.3 on 2019-08-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20190827_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('OnShipping', 'OnShipping'), ('Accepted', 'Accepted'), ('NEW', 'New'), ('Preparing', 'Preparing'), ('Refused', 'Refused')], default='New', max_length=15),
        ),
    ]
