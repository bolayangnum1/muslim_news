from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Registration(models.Model):

    class Meta:
        verbose_name = "данные пользователя"
        verbose_name_plural = "данные пользователей"

    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    fio = models.CharField(verbose_name='ФИО', max_length=200)
    dateofbirth = models.DateField(verbose_name='Дата рождения')
    city = models.CharField(verbose_name='Город', max_length=100)
    workexperience = models.CharField(verbose_name='Стаж работы', max_length=255)
    levelstudies = models.CharField(verbose_name='Уровень образования', max_length=100)

    def __str__(self):
        return self.fio


class Vacancy(models.Model):
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return str(self.requirements)

    name = models.CharField(verbose_name="ФИО", max_length=100)
    company = models.CharField(verbose_name="Компания", max_length=500)
    requirements = models.TextField(verbose_name="Требования", max_length=1000)
    salary = models.DecimalField(verbose_name="Зарплата", decimal_places=2, max_digits=100)
    duties = models.TextField(verbose_name="Обязанности")
    conditions = models.TextField(verbose_name="Условия для религиозных", max_length=1000)
