# Generated by Django 3.0.3 on 2020-06-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
