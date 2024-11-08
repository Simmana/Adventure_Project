from django.db import models
from pytils.translit import slugify
from datetime import datetime


class Category(models.Model):
    image = models.ImageField(blank=True, upload_to='image')
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Place(models.Model):
    name = models.CharField("Название места", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    image = models.ImageField(blank=True, upload_to='images')
    description = models.TextField("Об этом месте")
    address = models.CharField("Адрес места", max_length=150)
    salary = models.CharField("Стоимость", max_length=100)
    phone = models.CharField("Номер телефона", max_length=17)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)
    
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.name
    
class Zapis(models.Model):
    name = models.CharField("Запись", max_length=255)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.name