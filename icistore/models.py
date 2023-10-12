from django.db import models
from django.utils import timezone


class ImageModel(models.Model):
    image = models.ImageField(upload_to=f"{timezone.now().year}/{timezone.now().month:02d}/{timezone.now().day:02d}")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

    def __str__(self):
        return f"Image {self.pk}"


class Material(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    subtitle = models.CharField(max_length=200, verbose_name="Вид")
    meta_description = models.TextField(blank=True, null=True, verbose_name="SEO описание")
    meta_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name="SEO ключеве слова")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    materials = models.ManyToManyField(Material, blank=True, verbose_name="Материал ткани")
    manufacturer = models.CharField(max_length=100, blank=True, verbose_name="Производитель")
    country = models.CharField(max_length=100, blank=True, verbose_name="Страна")
    delivery_days = models.IntegerField(default=0, verbose_name="Доставка в днях")
    warranty = models.CharField(max_length=100, blank=True, verbose_name="гарантия")
    price = models.IntegerField(default=False, blank=True, verbose_name="Цена")
    images = models.ManyToManyField(ImageModel, blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    is_top_product = models.BooleanField(default=False, verbose_name="Популярный")

    def __str__(self):
        return f'Filter for {self.title}'


class Sofa(Product):
    # Другие поля для описания диванов
    class Meta:
        verbose_name = "Диван"
        verbose_name_plural = "Диваны"

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
    form = models.CharField(max_length=50, choices=form_choices, verbose_name="Форма")
    size = models.CharField(max_length=50, choices=size_choices, verbose_name="Размер")
    has_sleeper = models.BooleanField(default=False, verbose_name="Спальное место")


class InteriorSofa(Product):
    appearance_choices = [
        ('с высокой спинкой', 'С высокой спинкой'),
        ('с невысокой спинкой', 'С невысокой спинкой'),
    ]

    legs_choices = [
        ('металл', 'Металл'),
        ('бук', 'Бук'),
    ]
    appearance = models.CharField(max_length=50, choices=appearance_choices, verbose_name="Спинка")
    legs = models.CharField(max_length=50, choices=legs_choices, verbose_name="Материал")
    has_armrests = models.BooleanField(default=False, verbose_name="Спальное место")

    class Meta:
        verbose_name = "Интерьерный диван"
        verbose_name_plural = "Интерьерные диваны"
    # Другие поля для описания интерьерных диванов


class Chair(Product):
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

    appearance = models.CharField(max_length=50, choices=appearance_choices, verbose_name="Спинка")
    form = models.CharField(max_length=50, choices=form_choices, verbose_name="Форма")
    legs = models.CharField(max_length=50, choices=legs_choices, verbose_name="Материал")

    class Meta:
        verbose_name = "Кресло"
        verbose_name_plural = "Кресла"
    # Другие поля для описания кресел


class Ottoman(Product):
    form_choices = [
        ('круглая', 'Круглая'),
        ('прямоугольная', 'Прямоугольная'),
    ]

    legs_choices = [
        ('металл', 'Металл'),
        ('бук', 'Бук'),
    ]

    form = models.CharField(max_length=50, choices=form_choices, verbose_name="Форма")
    legs = models.CharField(max_length=50, choices=legs_choices, verbose_name="Материал")

    class Meta:
        verbose_name = "Пуф"
        verbose_name_plural = "Пуфы"
