# Generated by Django 4.0.3 on 2022-04-09 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_time', models.TimeField(verbose_name='Фаджр')),
                ('second_time', models.TimeField(verbose_name='Восход')),
                ('third_time', models.TimeField(verbose_name='Зухр')),
                ('fourth_time', models.TimeField(verbose_name='Аср')),
                ('fifth_time', models.TimeField(verbose_name='Магриб')),
                ('sixth_time', models.TimeField(verbose_name='Иша')),
                ('date', models.DateField(null=True, verbose_name='Дата')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='times.location')),
            ],
            options={
                'verbose_name': 'Время',
                'verbose_name_plural': 'Времена',
            },
        ),
    ]
