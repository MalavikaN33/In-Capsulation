# Generated by Django 2.2 on 2020-08-19 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mgm', '0002_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='ID',
            new_name='supplierid',
        ),
    ]
