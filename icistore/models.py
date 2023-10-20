from django.db import models
from django.utils import timezone


class ImageModel(models.Model):
    image = models.ImageField(upload_to=f"{timezone.now().year}/{timezone.now().month:02d}/{timezone.now().day:02d}")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

    def __str__(self):
        return f"Image {self.pk}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    images = models.ImageField( blank=True, verbose_name="Иконка категории", default="", null=True)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
class Material(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(blank=True, verbose_name="Иконка материала", default="")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name






    def __str__(self):
        return self.name

class FormProduct(models.Model):
    title = models.CharField(max_length=120, verbose_name="Форма")
    category = models.ManyToManyField(Category, verbose_name="Категория", blank=True)

    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Форма"

    def __str__(self):
        return self.title

class Size(models.Model):
    sizeL = models.CharField(max_length=120, verbose_name="Длина")
    sizeW = models.CharField(max_length=120, verbose_name="Ширина")
    sizeH = models.CharField(max_length=120, verbose_name="Высота")
    category = models.ManyToManyField(Category, verbose_name="Категория",  blank=True)
    class Meta:
        verbose_name = "Габаритные размеры"
        verbose_name_plural = "Габаритные размеры"

    def __str__(self):
        return f"{self.sizeL}, {self.sizeW}, {self.sizeH}"

class Sleeper(models.Model):
    title = models.CharField(max_length=20,verbose_name="спальное место")
    category = models.ManyToManyField(Category, verbose_name="Категория",  blank=True)
    class Meta:
        verbose_name = "спальное место"
        verbose_name_plural = "спальное место"
    def __str__(self):
        return f"{self.title}"


class Supports(models.Model):
    title = models.CharField(max_length=20,verbose_name="Опоры")
    category = models.ManyToManyField(Category, verbose_name="Категория",  blank=True)
    class Meta:
        verbose_name = "Опоры"
        verbose_name_plural = "Опоры"
    def __str__(self):
        return f"{self.title}"
class Armrests(models.Model):
    title = models.CharField(max_length=20,verbose_name="Подлокотники")
    category = models.ManyToManyField(Category,  verbose_name="Категория", blank=True)
    class Meta:
        verbose_name = "Подлокотники"
        verbose_name_plural = "Подлокотники"
    def __str__(self):
        return f"{self.title}"



class Appearance(models.Model):
    title = models.CharField(max_length=120, verbose_name="Форма спинки")
    category = models.ManyToManyField(Category, verbose_name="Категория",  blank=True)
    class Meta:
        verbose_name = "Форма спинки"
        verbose_name_plural = "Форма спинки"
    def __str__(self):
        return self.title


class Legs(models.Model):
    title = models.CharField(max_length=120, verbose_name="Материал изделия")
    category = models.ManyToManyField(Category, verbose_name="Категория", blank=True)
    class Meta:
        verbose_name = "Материал изделия"
        verbose_name_plural = "Материал изделия"
    def __str__(self):
        return self.title
class Type(models.Model):
    name = models.CharField(max_length=150 , verbose_name="Вид продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Вид изделия"
        verbose_name_plural = "Вид изделия"

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название", unique=True)
    subtitle = models.ForeignKey(Type, on_delete=models.CASCADE, null=True ,blank=True, verbose_name="Вид")
    description = models.TextField(blank=True, null=True, verbose_name="описание")
    meta_description = models.TextField(blank=True, null=True, verbose_name="SEO описание")
    meta_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name="SEO ключеве слова")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", null=True, blank=True)

    materials = models.ManyToManyField(Material, blank=True, verbose_name="Материал ткани",)
    images = models.ManyToManyField(ImageModel, blank=True, verbose_name="Фото", )
    form = models.ForeignKey(FormProduct, on_delete=models.CASCADE, verbose_name="Форма", null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name="Размер (Д x Ш x В)", null=True, blank=True)
    has_sleeper = models.ForeignKey(Sleeper, on_delete=models.CASCADE, verbose_name="спальное место", null=True, blank=True)
    appearance = models.ForeignKey(Appearance, on_delete=models.CASCADE, verbose_name="Форма спинки", null=True, blank=True)
    supports = models.ForeignKey(Supports, on_delete=models.CASCADE, verbose_name="Опоры", null=True, blank=True)
    armrests = models.ForeignKey(Armrests, on_delete=models.CASCADE, verbose_name="Подлокотники", null=True, blank=True)




    manufacturer = models.CharField(max_length=100, blank=True, verbose_name="Производитель")
    country = models.CharField(max_length=100, blank=True, verbose_name="Страна")
    delivery_days = models.IntegerField(default=0, verbose_name="Доставка в днях")
    warranty = models.CharField(max_length=100, blank=True, verbose_name="гарантия")
    price = models.IntegerField(default=False, blank=True, verbose_name="Цена")

    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    is_top_product = models.BooleanField(default=False, verbose_name="Популярный")
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    def __str__(self):
        return f'{self.title}'










# Для главной страницы


class MainPageContent(models.Model):
    video = models.FileField(upload_to=f"{timezone.now().year}/{timezone.now().month:02d}/{timezone.now().day:02d}", null=True, blank=True, verbose_name="Видео")
    videoImage = models.ImageField(upload_to=f"{timezone.now().year}/{timezone.now().month:02d}/{timezone.now().day:02d}", null=True, blank=True, verbose_name="Картинка Видео")
    advantages = models.ManyToManyField('Advantage', verbose_name="Преимущества")

    class Meta:
        verbose_name = "Видео для главной страницы"
        verbose_name_plural = "Видео для главной страницы"
    def __str__(self):
        return "Main Page Content"

class Advantage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=100, verbose_name="Подзаголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to=f"{timezone.now().year}/{timezone.now().month:02d}/{timezone.now().day:02d}", verbose_name="Заголовок")

    class Meta:
        verbose_name = "Преимущества для главной страницы"
        verbose_name_plural = "Преимущества для главной страницы"
    def __str__(self):
        return self.title