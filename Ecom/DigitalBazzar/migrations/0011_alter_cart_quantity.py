# Generated by Django 3.2.9 on 2022-01-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalBazzar', '0010_auto_20220104_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]