# Generated by Django 3.2 on 2021-04-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
