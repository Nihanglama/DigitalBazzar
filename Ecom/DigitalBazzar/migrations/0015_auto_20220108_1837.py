# Generated by Django 3.2.9 on 2022-01-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalBazzar', '0014_auto_20220106_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]