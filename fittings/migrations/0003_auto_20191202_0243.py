# Generated by Django 2.2.4 on 2019-12-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fittings', '0002_auto_20191201_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fittingitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]