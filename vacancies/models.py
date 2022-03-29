from django.db import models


class Vacancy(models.Model):
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return str(self.requirements)

    name = models.CharField(verbose_name="ФИО", max_length=100)
    company = models.CharField(verbose_name="Компания", max_length=500)
    requirements = models.TextField(verbose_name="Требования", max_length=1000)
    salary = models.IntegerField(verbose_name="Зарплата", default=0)
    duties = models.TextField(verbose_name="Обязанности")
    conditions = models.TextField(verbose_name="Условия для религиозных", max_length=1000)
