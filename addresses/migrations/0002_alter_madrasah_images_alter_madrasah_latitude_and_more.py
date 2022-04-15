# Generated by Django 4.0.3 on 2022-04-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madrasah',
            name='images',
            field=models.ImageField(upload_to='media', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='madrasah',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='madrasah',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='images',
            field=models.ImageField(upload_to='media', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='mosquecollege',
            name='images',
            field=models.ImageField(upload_to='media', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='mosquecollege',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mosquecollege',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='mosquelibrary',
            name='images',
            field=models.ImageField(upload_to='media', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='mosquelibrary',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mosquelibrary',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='mosqueroom',
            name='images',
            field=models.ImageField(upload_to='media', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='mosqueroom',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mosqueroom',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='mosqueuniversity',
            name='images',
            field=models.ImageField(upload_to='media', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='mosqueuniversity',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mosqueuniversity',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
    ]