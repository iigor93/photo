import secrets
import string

from django.db import models
from django.utils.safestring import mark_safe


class Carousel(models.Model):
    class Meta:
        verbose_name = "Страница карусели"
        verbose_name_plural = "Страницы карусели"
        ordering = ('id',)

    image = models.ImageField(verbose_name="Изображение", upload_to='carousel/%Y/%m/')
    title = models.CharField(max_length=50, verbose_name="Заголовок", null=True, blank=True)
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True)
    link = models.CharField(max_length=100, verbose_name="Ссылка", null=True, blank=True)
    active = models.BooleanField(verbose_name="Показ в карусели", default=True)

    def image_thumb(self):
        return mark_safe('<img src="/media/%s" height=50>' % self.image)

    def __str__(self):
        return self.title


class Advantage(models.Model):
    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
        ordering = ('id',)

    image = models.ImageField(verbose_name="Изображение", upload_to='advantage/%Y/%m/')
    title = models.CharField(max_length=50, verbose_name="Заголовок", null=True, blank=True)
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True)
    active = models.BooleanField(verbose_name="Показ в карусели", default=True)

    def image_thumb(self):
        return mark_safe('<img src="/media/%s" height=50>' % self.image)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = "Категории фото в портфолио"
        verbose_name_plural = "Категории фото в портфолио"
        ordering = ('id',)

    name = models.CharField(max_length=100, verbose_name="Категория")
    image = models.ImageField(verbose_name="Изображение", upload_to='category/%Y/%m/', null=True)

    def image_thumb(self):
        return mark_safe('<img src="/media/%s" height=50>' % self.image)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"
        ordering = ('id',)

    WH_CHOICES = (
        (" ", "Нет"),
        ("large-width", "Широкие"),
        ("large-height", "Высокие"),
        ("large-width large-height", "Высокие и широкие"),
    )

    image = models.ImageField(verbose_name="Изображение", upload_to='portfolio/%Y/%m/')
    title = models.CharField(max_length=50, verbose_name="Заголовок", null=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name="Категория")
    wh_class = models.CharField(max_length=30, choices=WH_CHOICES, verbose_name="Высота Ширина", default="none")
    active = models.BooleanField(verbose_name="Показ", default=True)

    def image_thumb(self):
        return mark_safe('<img src="/media/%s" height=50>' % self.image)

    def __str__(self):
        return self.title


class SubscribeEmail(models.Model):
    """ Email с формы в футере """

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
        ordering = ('date',)

    email = models.EmailField(verbose_name="Email", unique=True)
    date = models.DateField(auto_now_add=True, verbose_name="Дата добавления")
    delete_code = models.CharField(max_length=21, verbose_name="Код проверки для удаления", null=True)

    def save(self, *args, **kwargs):
        num = 20
        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
        self.delete_code = str(res)
        super(SubscribeEmail, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class Contact(models.Model):
    """ Contact info """

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Email")


class About(models.Model):
    """ О нас """

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    image = models.ImageField(verbose_name="Изображение", upload_to='about/%Y/%m/')
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.CharField(max_length=1024, verbose_name="Описание")
