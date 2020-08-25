# Generated by Django 2.2.3 on 2019-08-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20190827_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Preparing', 'Preparing'), ('NEW', 'New'), ('Completed', 'Completed'), ('Refused', 'Refused'), ('OnShipping', 'OnShipping'), ('Accepted', 'Accepted')], default='New', max_length=15),
        ),
    ]
