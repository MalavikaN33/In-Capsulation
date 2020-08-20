# Generated by Django 2.2 on 2020-08-20 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgm', '0007_supplier_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('firstname', models.CharField(max_length=30, null=True)),
                ('lastname', models.CharField(max_length=30, null=True)),
                ('business', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
        ),
    ]