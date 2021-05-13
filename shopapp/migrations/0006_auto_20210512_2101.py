# Generated by Django 3.2 on 2021-05-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='unit_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
