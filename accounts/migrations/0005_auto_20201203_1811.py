# Generated by Django 3.1.3 on 2020-12-03 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201201_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_number',
            field=models.IntegerField(blank=True, default=360634781732),
        ),
    ]