import os
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"Image {self.id}"
class ImageModel(models.Model):
    image = models.ImageField(upload_to=f"{timezone.now().year}/{timezone.now().month:02d}/{timezone.now().day:02d}")


    def __str__(self):
        return f"Image {self.pk}"
class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sofa(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    
    title = models.CharField(max_length=200, verbose_name="Название")
    subtitle = models.CharField(max_length=200, verbose_name="Вид")
    materials = models.ManyToManyField(Material, blank=True, verbose_name="Материал ткани")
    manufacturer = models.CharField(max_length=100, blank=True, verbose_name="Производитель")
    country = models.CharField(max_length=100, blank=True, verbose_name="Страна")
    delivery_days = models.IntegerField(default=0, verbose_name="Доставка в днях")
    warranty = models.CharField(max_length=100, blank=True, verbose_name="гарантия")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    is_top_product = models.BooleanField(default=False, verbose_name="Популярный")
    price = models.IntegerField(default=False, blank=True, verbose_name="Цена")
    images = models.ManyToManyField(ImageModel, blank=True, verbose_name="Фото")
    
    # Другие поля для описания диванов

    def __str__(self):
        return self.name


class SofaFilter(models.Model):
    form_choices = [
        ('эркерный', 'Эркерный'),
        ('модульный', 'Модульный'),
        ('прямой', 'Прямой'),
        ('угловой', 'Угловой'),
    ]

    size_choices = [
        ('до 2000мм', 'До 2000мм'),
        ('2000-3000мм', '2000-3000мм'),
        ('свыше 3000мм', 'Свыше 3000мм'),
    ]

    sofa = models.ForeignKey('Sofa', on_delete=models.CASCADE)
    form = models.CharField(max_length=50, choices=form_choices, verbose_name="Форма")
    size = models.CharField(max_length=50, choices=size_choices, verbose_name="Размер")
    has_sleeper = models.BooleanField(default=False, verbose_name="Спальное место")

    def __str__(self):
        return f'Filter for {self.sofa.name}'

class InteriorSofa(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    
    title = models.CharField(max_length=200, verbose_name="Название")
    subtitle = models.CharField(max_length=200, verbose_name="Вид")
    materials = models.ManyToManyField(Material, blank=True, verbose_name="Материал ткани")
    manufacturer = models.CharField(max_length=100, blank=True, verbose_name= "Производитель")
    country = models.CharField(max_length=100, blank=True,verbose_name="Страна")
    delivery_days = models.IntegerField(default=0, verbose_name="Доставка в днях")
    warranty = models.CharField(max_length=100, blank=True, verbose_name="гарантия")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    is_top_product = models.BooleanField(default=False, verbose_name="Популярный")
    price = models.IntegerField(default=False, blank=True, verbose_name="Цена")
    images = models.ManyToManyField(ImageModel, blank=True, verbose_name="Фото")
    
    # Другие поля для описания интерьерных диванов

    def __str__(self):
        return self.name


class InteriorSofaFilter(models.Model):
    appearance_choices = [
        ('с высокой спинкой', 'С высокой спинкой'),
        ('с невысокой спинкой', 'С невысокой спинкой'),
    ]

    legs_choices = [
        ('металл', 'Металл'),
        ('бук', 'Бук'),
    ]

    interior_sofa = models.ForeignKey('InteriorSofa', on_delete=models.CASCADE)
    appearance = models.CharField(max_length=50, choices=appearance_choices, verbose_name="Спинка")
    legs = models.CharField(max_length=50, choices=legs_choices, verbose_name="Материал")
    has_armrests = models.BooleanField(default=False, verbose_name="Спальное место")

    def __str__(self):
        return f'Filter for {self.interior_sofa.name}'

class Chair(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    
    title = models.CharField(max_length=200, verbose_name="Название")
    subtitle = models.CharField(max_length=200, verbose_name="Вид")
    materials = models.ManyToManyField(Material, blank=True, verbose_name="Материал ткани")
    manufacturer = models.CharField(max_length=100, blank=True, verbose_name="Производитель")
    country = models.CharField(max_length=100, blank=True, verbose_name="Страна")
    delivery_days = models.IntegerField(default=0, verbose_name="Доставка в днях")
    warranty = models.CharField(max_length=100, blank=True, verbose_name="гарантия")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    is_top_product = models.BooleanField(default=False, verbose_name="Популярный")
    price = models.IntegerField(default=False, blank=True, verbose_name="Цена")
    images = models.ManyToManyField(ImageModel, blank=True, verbose_name="Фото")
    
    # Другие поля для описания кресел

    def __str__(self):
        return self.name


class ChairFilter(models.Model):
    appearance_choices = [
        ('с высокой спинкой', 'С высокой спинкой'),
        ('с невысокой спинкой', 'С невысокой спинкой'),
    ]

    form_choices = [
        ('круглая', 'Круглая'),
        ('прямоугольная', 'Прямоугольная'),
    ]

    legs_choices = [
        ('металл', 'Металл'),
        ('бук', 'Бук'),
    ]

    chair = models.ForeignKey('Chair', on_delete=models.CASCADE, )
    appearance = models.CharField(max_length=50, choices=appearance_choices, verbose_name="Спинка")
    form = models.CharField(max_length=50, choices=form_choices, verbose_name="Форма")
    legs = models.CharField(max_length=50, choices=legs_choices, verbose_name="Материал")

    def __str__(self):
        return f'Filter for {self.chair.name}'

class Ottoman(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    
    title = models.CharField(max_length=200, verbose_name="Название")
    subtitle = models.CharField(max_length=200, verbose_name="Вид")
    materials = models.ManyToManyField(Material, blank=True, verbose_name="Материал ткани")
    manufacturer = models.CharField(max_length=100, blank=True, verbose_name="Производитель")
    country = models.CharField(max_length=100, blank=True, verbose_name="Страна")
    delivery_days = models.IntegerField(default=0, verbose_name="Доставка в днях")
    warranty = models.CharField(max_length=100, blank=True, verbose_name="гарантия")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    is_top_product = models.BooleanField(default=False, verbose_name="Популярный")
    price = models.IntegerField(default=False, blank=True, verbose_name="Цена")
    images = models.ManyToManyField(ImageModel, blank=True, verbose_name="Фото")
    
    # Другие поля для описания пуфов

    def __str__(self):
        return self.name


class OttomanFilter(models.Model):
    form_choices = [
        ('круглая', 'Круглая'),
        ('прямоугольная', 'Прямоугольная'),
    ]

    legs_choices = [
        ('металл', 'Металл'),
        ('бук', 'Бук'),
    ]

    ottoman = models.ForeignKey('Ottoman', on_delete=models.CASCADE)
    form = models.CharField(max_length=50, choices=form_choices, verbose_name="Форма")
    legs = models.CharField(max_length=50, choices=legs_choices, verbose_name="Материал")

    def __str__(self):
        return f'Filter for {self.ottoman.name}'
