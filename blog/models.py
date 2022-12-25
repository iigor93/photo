from django.db import models
from django.utils.safestring import mark_safe


class BlogTag(models.Model):
    """ Теги для блога """
    class Meta:
        verbose_name = "Тег для блога"
        verbose_name_plural = "Теги для блога"
        ordering = ('id',)

    name = models.CharField(max_length=100, verbose_name="Тег")

    def __str__(self):
        return self.name


class BlogImage(models.Model):
    """ Фото для блога """
    class Meta:
        verbose_name = "Фото блога"
        verbose_name_plural = "Фото блогов"
        ordering = ('id',)

    image = models.ImageField(verbose_name="Фото", upload_to="blog/%Y/%m/")
    name = models.CharField(max_length=50, verbose_name="Описание")

    def image_thumb(self):
        return mark_safe('<img src="/media/%s" height=50>' % self.image)

    def __str__(self):
        return self.name


class BlogItem(models.Model):
    """ Blog """
    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блогов"
        ordering = ("date",)

    date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    main_tag = models.ForeignKey(BlogTag, verbose_name="Главный тег", null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(BlogTag, verbose_name="Теги", related_name="blog_item")
    main_photo = models.ImageField(verbose_name="Главное фото", upload_to="blog/%Y/%m/")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    top_text = models.CharField(max_length=2048, verbose_name="Вступление", null=True, blank=True)
    quote = models.CharField(max_length=1024, verbose_name="Цитата", null=True, blank=True)
    description = models.CharField(max_length=2048, verbose_name="Описание", null=True, blank=True)
    last_description = models.CharField(max_length=2048, verbose_name="Окончание", null=True, blank=True)
    image = models.ManyToManyField(BlogImage, verbose_name="Фото в тексте блога")

    def image_thumb(self):
        return mark_safe('<img src="/media/%s" height=50>' % self.main_photo)

    def __str__(self):
        return f"{self.title}, {self.date}"
