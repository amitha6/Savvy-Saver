# Generated by Django 2.2.6 on 2019-11-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_auto_20191109_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
