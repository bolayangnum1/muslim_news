from django.db import models


class Cafe(models.Model):
    class Meta:
        verbose_name = "Кафе"
        verbose_name_plural = "Кафе"

    name = models.CharField(verbose_name="Название кафе", max_length=300)
    certificate = models.BooleanField(verbose_name="Сертификат халал присутствует", default=True)
    mosqueroom = models.BooleanField(verbose_name="Намазкана есть/нет", default=True)
    contacts = models.CharField(verbose_name="Контакты", max_length=16)
    address = models.CharField(verbose_name="Адресс", max_length=500)
    images = models.ImageField(verbose_name="Фотографии")
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=100, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)
    is_published = models.BooleanField(default=False, verbose_name='активировать')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

    name = models.CharField(verbose_name="Название ресторана", max_length=300)
    bighall = models.IntegerField(verbose_name="Банкетный зал на сколько человек?", default=80)
    certificate = models.BooleanField(verbose_name="Сертификат халал присутствует", default=True)
    mosqueroom = models.BooleanField(verbose_name="Намазкана есть/нет", default=True)
    contacts = models.CharField(verbose_name="Контакты", max_length=16)
    address = models.CharField(verbose_name="Адресс", max_length=500)
    images = models.ImageField(verbose_name="Фотографии", upload_to=None)
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=100, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)
    is_published = models.BooleanField(default=False, verbose_name='активировать')

    def __str__(self):
        return self.name


class Magazine(models.Model):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    name = models.CharField(verbose_name="Название магазина/нипермаркета", max_length=300)
    site = models.CharField(verbose_name="Сайт магазина/гипермаркета", max_length=100, blank=True)
    alcohol = models.BooleanField(verbose_name="Спритное продается да/нет", default=False)
    productsCertificate = models.BooleanField(verbose_name="Продукты халалные  есть/нет", default=True)
    worktime = models.CharField(verbose_name="Режим работы от/до", max_length=200)
    certificate = models.BooleanField(verbose_name="Сертификат халал присутствует", default=True)
    mosqueroom = models.BooleanField(verbose_name="Намазкана есть/нет", default=True)
    contacts = models.CharField(verbose_name="Контакты", max_length=16)
    address = models.CharField(verbose_name="Адресс", max_length=500)
    images = models.ImageField(verbose_name="Фотографии", upload_to=None)
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=100, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)
    is_published = models.BooleanField(default=False, verbose_name='активировать')

    def __str__(self):
        return self.name


class FastFood(models.Model):
    class Meta:
        verbose_name = "Фаст Фуд"
        verbose_name_plural = "Фаст Фуды"

    name = models.CharField(verbose_name="Название фаст-фуд", max_length=300)
    worktime = models.CharField(verbose_name="Режим работы от/до", max_length=200)
    site = models.URLField(verbose_name="Сайт", max_length=100, blank=True)
    certificate = models.BooleanField(verbose_name="Сертификат халал присутствует", default=True)
    mosqueroom = models.BooleanField(verbose_name="Намазкана есть/нет", default=True)
    contacts = models.CharField(verbose_name="Контакты", max_length=16)
    address = models.CharField(verbose_name="Адресс", max_length=500)
    images = models.ImageField(verbose_name="Фотографии", upload_to=None)
    longitude = models.DecimalField(verbose_name='Долгота', decimal_places=100, max_digits=1000)
    latitude = models.DecimalField(verbose_name='Широта', decimal_places=100, max_digits=1000)
    is_published = models.BooleanField(default=False, verbose_name='активировать')

    def __str__(self):
        return self.name