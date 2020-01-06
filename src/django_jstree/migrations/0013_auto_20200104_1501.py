# Generated by Django 3.0.1 on 2020-01-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_jstree', '0012_auto_20200104_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popupmenuitem',
            name='childMenuItems',
            field=models.ManyToManyField(blank=True, related_name='parentMenuItems', to='django_jstree.popupMenuItem', verbose_name='Child Menu Items'),
        ),
    ]
