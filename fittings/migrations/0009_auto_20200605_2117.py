# Generated by Django 2.2.12 on 2020-06-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fittings', '0008_auto_20200605_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unicategory',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Groups listed here will be able to access fits and doctrines listed under this category. If a category has no groups listed then it is considered an public category, accessible to anyone with permission to access permissions to the fittings module.', related_name='access_restricted_category', to='auth.Group'),
        ),
    ]
