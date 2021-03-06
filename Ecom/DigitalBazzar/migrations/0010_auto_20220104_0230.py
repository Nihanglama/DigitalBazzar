# Generated by Django 3.2.9 on 2022-01-04 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalBazzar', '0009_cart_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='name',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DigitalBazzar.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
