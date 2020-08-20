# Generated by Django 2.2 on 2020-08-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgm', '0008_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30, null=True)),
                ('level', models.IntegerField(null=True)),
                ('done', models.IntegerField(null=True)),
            ],
        ),
    ]