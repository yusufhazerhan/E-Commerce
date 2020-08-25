# Generated by Django 2.2.3 on 2019-08-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20190823_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Refused', 'Refused'), ('Accepted', 'Accepted'), ('OnShipping', 'OnShipping'), ('Preparing', 'Preparing'), ('NEW', 'New'), ('Completed', 'Completed')], default='New', max_length=15),
        ),
    ]
