from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(verbose_name="Название категории", max_length=100)


class BaseAbstractCategory(models.Model):
    class Meta:
        abstract = True

    certificate = models.BooleanField(verbose_name="Сертификат халал присутствует", default=True)
    mosqueRoom = models.BooleanField(verbose_name="Намазкана есть/нет", default=True)
    contacts = models.CharField(verbose_name="Контакты", max_length=16)
    address = models.CharField(verbose_name="Адресс", max_length=500)
    images = models.ImageField(verbose_name="Фотографии")
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=100, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)


class MosqueCafe(BaseAbstractCategory):
    class Meta:
        verbose_name = "Кафе"
        verbose_name_plural = "Кафе"

    name = models.CharField(verbose_name="Название кафе", max_length=300)


class Restaurant(BaseAbstractCategory):
    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

    name = models.CharField(verbose_name="Название ресторана", max_length=300)
    bigHall = models.IntegerField(verbose_name="Банкетный зал на сколько человек?", default=80)
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=100, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)


class Magazine(BaseAbstractCategory):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    name = models.CharField(verbose_name="Название магазина/нипермаркета", max_length=300)
    site = models.CharField(verbose_name="Сайт магазина/гипермаркета", max_length=100)
    alcohol = models.BooleanField(verbose_name="Спритное продается да/нет", default=False)
    productsCertificate = models.BooleanField(verbose_name="Продукты халалные  есть/нет", default=True)
    workTime = models.CharField(verbose_name="Режим работы от/до", max_length=200)
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=100, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)


class FastFood(BaseAbstractCategory):
    class Meta:
        verbose_name = "Фаст Фуд"
        verbose_name_plural = "Фаст Фуды"

    name = models.CharField(verbose_name="Название фаст-фуд", max_length=300)
    workTime = models.CharField(verbose_name="Режим работы от/до", max_length=200)
    site = models.CharField(verbose_name="Сайт", max_length=100)
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=000, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)