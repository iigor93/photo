from django.db import models


class Price(models.Model):
    """ Цена """

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        ordering = ("price",)

    price = models.PositiveIntegerField(verbose_name="Цена в руб, без копеек", default=0)
    name = models.CharField(max_length=50, verbose_name="Название", help_text="Стандарт, Премиум и т.д.")
    duration = models.CharField(max_length=50, verbose_name="Продолжительность", help_text="1 час, 2 часа, 1 день")
    description_1 = models.CharField(max_length=50, verbose_name="Описание 1")
    description_2 = models.CharField(max_length=50, verbose_name="Описание 2")
    description_3 = models.CharField(max_length=50, verbose_name="Описание 3")
    description_4 = models.CharField(max_length=50, verbose_name="Описание 4")


class Faq(models.Model):
    """ FAQ """

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ("number",)

    number = models.SmallIntegerField(verbose_name="Номер")
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.CharField(max_length=1024, verbose_name="Описание")
