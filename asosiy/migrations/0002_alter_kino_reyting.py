# Generated by Django 4.1.2 on 2022-10-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kino',
            name='reyting',
            field=models.FloatField(),
        ),
    ]
