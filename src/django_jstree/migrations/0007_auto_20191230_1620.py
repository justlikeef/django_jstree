# Generated by Django 3.0 on 2019-12-30 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_jstree', '0006_auto_20191230_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nodetype',
            old_name='jsTree',
            new_name='jstrees',
        ),
    ]