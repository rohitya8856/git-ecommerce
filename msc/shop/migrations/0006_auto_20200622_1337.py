# Generated by Django 3.0.3 on 2020-06-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address2',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='orders',
            name='number',
            field=models.CharField(default='', max_length=11),
        ),
    ]