from django.db import models


GENDER_CHOICES = (
    (0, 'Мужской'),
    (1, 'Женский')
)


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(verbose_name="Название категории", max_length=200)

    def __str__(self):
        return self.name


class BaseAbstractCategory(models.Model):
    class Meta:
        abstract = True

    address = models.CharField(verbose_name="Адрес", max_length=500)
    contacts = models.CharField(verbose_name="Контакты", max_length=24)
    images = models.ImageField(verbose_name="Фотографии", upload_to='files/images/')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Mosque(BaseAbstractCategory):
    class Meta:
        verbose_name = "Мечеть"
        verbose_name_plural = "Мечети"

    name = models.CharField(verbose_name="Имя мечети", max_length=500)

    def __str__(self):
        return self.name


class MosqueRoom(BaseAbstractCategory):
    class Meta:
        verbose_name = "Моельная комната"
        verbose_name_plural = "Молельные комнаты"

    name = models.CharField(verbose_name="Имя молельной комнаты", max_length=500)
    gender = models.IntegerField(verbose_name="Пол", choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class MosqueCollege(BaseAbstractCategory):
    class Meta:
        verbose_name = "Исламский колледж"
        verbose_name_plural = "Исламские колледжи"

    name = models.CharField(verbose_name="Имя колледжа", max_length=500)

    def __str__(self):
        return self.name


class MosqueUniversity(BaseAbstractCategory):
    class Meta:
        verbose_name = "Исламский университет"
        verbose_name_plural = "Исламские университеты"

    name = models.CharField(verbose_name="Имя университета", max_length=500)

    def __str__(self):
        return self.name


class Madrasah(BaseAbstractCategory):
    class Meta:
        verbose_name = "Медресе"
        verbose_name_plural = "Медресе"

    name = models.CharField(verbose_name="Имя медресе", max_length=500, null=True)

    def __str__(self):
        return self.name


class MosqueLibrary(BaseAbstractCategory):
    class Meta:
        verbose_name = "Исламская библиотека"
        verbose_name_plural = "Исламские библиотеки"

    name = models.CharField(verbose_name="Имя библиотеки", max_length=500)
    work_time = models.TimeField(verbose_name="Время работы")

    def __str__(self):
        return self.name