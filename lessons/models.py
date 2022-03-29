from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name = "Категория для урока"
        verbose_name_plural = "Категории для уроков"

    name = models.CharField(verbose_name='Категория для уроков', max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    name = models.CharField(verbose_name='Название урока', max_length=1000)
    author = models.CharField(verbose_name='Автор', max_length=500)
    audio = models.URLField(verbose_name='Аудио')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return f'{self.name}'