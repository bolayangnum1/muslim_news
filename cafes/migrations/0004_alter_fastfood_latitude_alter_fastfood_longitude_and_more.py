# Generated by Django 4.0.3 on 2022-03-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0003_mosquecafe_latitude_mosquecafe_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastfood',
            name='latitude',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='fastfood',
            name='longitude',
            field=models.DecimalField(decimal_places=0, max_digits=1000, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='latitude',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='longitude',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='mosquecafe',
            name='latitude',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mosquecafe',
            name='longitude',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='bigHall',
            field=models.IntegerField(default=80, verbose_name='Банкетный зал на сколько человек?'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Долгота'),
        ),
    ]
