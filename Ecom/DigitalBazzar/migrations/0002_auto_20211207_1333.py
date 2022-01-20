# Generated by Django 3.2.9 on 2021-12-07 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalBazzar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('cloths', 'cloths'), ('food', 'food'), ('shoes', 'shoes'), ('iots', 'iots'), ('books', 'books'), ('sports', 'sports')], max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='DigitalBazzar.category'),
        ),
    ]