# Generated by Django 3.2.9 on 2022-01-03 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalBazzar', '0008_alter_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DigitalBazzar.order'),
        ),
    ]
