# Generated by Django 2.2.3 on 2019-08-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190823_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('OnShipping', 'OnShipping'), ('Preparing', 'Preparing'), ('Refused', 'Refused'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='New', max_length=15),
        ),
    ]
