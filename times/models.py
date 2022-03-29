from django.db import models


class Location(models.Model):
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    location = models.CharField(verbose_name="Локация", max_length=200)

    def __str__(self):
        return f'{self.location}'


class Time(models.Model):
    class Meta:
        verbose_name = "Время"
        verbose_name_plural = "Времена"

    first_time = models.TimeField(verbose_name="Фаджр")
    second_time = models.TimeField(verbose_name="Восход")
    third_time = models.TimeField(verbose_name="Зухр")
    fourth_time = models.TimeField(verbose_name="Аср")
    fifth_time = models.TimeField(verbose_name="Магриб")
    sixth_time = models.TimeField(verbose_name="Иша")
    date = models.DateField(verbose_name="Дата", null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.date}'