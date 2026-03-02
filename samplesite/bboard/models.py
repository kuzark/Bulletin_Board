from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Содержание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Опубликовано'
    )
    rubric = models.ForeignKey(
        'Rubric', 
        null=True, # Дает возможность создать столбец в уже заполненной БД
        on_delete=models.PROTECT, # При удалении рубрики, связанные с ней данные не удаляются
        verbose_name='Рубрика' # Человекочитаемое представление
    )

    def __str__(self):
        return self.title # Человекочитаемое представление одной записи

    class Meta: # Параметры модели без привязки к записям
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ('-published',) # Сортировка по умолчанию (- означает обратная)


class Rubric(models.Model):
    name = models.CharField(
        max_length=20, db_index=True, verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ('name',)
