# Generated by Django 2.2.12 on 2020-06-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fittings', '0007_auto_20200605_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unicategory',
            name='color',
            field=models.TextField(default='#FFFFFF', max_length=20),
        ),
    ]
