# Generated by Django 4.0.3 on 2022-03-31 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_vacancy_adress_vacancy_education_vacancy_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='registration',
        ),
        migrations.AddField(
            model_name='registration',
            name='vacancy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vacancies.vacancy', verbose_name='Заявка'),
            preserve_default=False,
        ),
    ]