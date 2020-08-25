# Generated by Django 2.2.3 on 2019-08-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20190827_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('OnShipping', 'OnShipping'), ('Accepted', 'Accepted'), ('Refused', 'Refused'), ('NEW', 'New'), ('Preparing', 'Preparing'), ('Completed', 'Completed')], default='New', max_length=15),
        ),
    ]