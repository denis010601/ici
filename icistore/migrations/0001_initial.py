# Generated by Django 4.2.6 on 2023-10-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Подзаголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='2023/10/18', verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Преимущества для главной страницы',
                'verbose_name_plural': 'Преимущества для главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Форма спинки')),
            ],
            options={
                'verbose_name': 'Форма спинки',
                'verbose_name_plural': 'Форма спинки',
            },
        ),
        migrations.CreateModel(
            name='Armrests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Подлокотники')),
            ],
            options={
                'verbose_name': 'Подлокотники',
                'verbose_name_plural': 'Подлокотники',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('images', models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='FormProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Форма')),
                ('category', models.ManyToManyField(blank=True, to='icistore.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Форма',
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='2023/10/18')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('images', models.ImageField(blank=True, default='', upload_to='', verbose_name='Иконка материала')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Вид продукта')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Supports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Опоры')),
                ('category', models.ManyToManyField(blank=True, to='icistore.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Опоры',
                'verbose_name_plural': 'Опоры',
            },
        ),
        migrations.CreateModel(
            name='Sleeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='спальное место')),
                ('category', models.ManyToManyField(blank=True, to='icistore.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'спальное место',
                'verbose_name_plural': 'спальное место',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizeL', models.CharField(max_length=120, verbose_name='Длина')),
                ('sizeW', models.CharField(max_length=120, verbose_name='Ширина')),
                ('sizeH', models.CharField(max_length=120, verbose_name='Высота')),
                ('category', models.ManyToManyField(blank=True, to='icistore.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Габаритные размеры',
                'verbose_name_plural': 'Габаритные размеры',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='SEO описание')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='SEO ключеве слова')),
                ('manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Производитель')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Страна')),
                ('delivery_days', models.IntegerField(default=0, verbose_name='Доставка в днях')),
                ('warranty', models.CharField(blank=True, max_length=100, verbose_name='гарантия')),
                ('price', models.IntegerField(blank=True, default=False, verbose_name='Цена')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('is_top_product', models.BooleanField(default=False, verbose_name='Популярный')),
                ('appearance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.appearance', verbose_name='Форма спинки')),
                ('armrests', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.armrests', verbose_name='Подлокотники')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.category', verbose_name='Категория')),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.formproduct', verbose_name='Форма')),
                ('has_sleeper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.sleeper', verbose_name='спальное место')),
                ('images', models.ManyToManyField(blank=True, to='icistore.imagemodel', verbose_name='Фото')),
                ('materials', models.ManyToManyField(blank=True, to='icistore.material', verbose_name='Материал ткани')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.size', verbose_name='Размер (Д x Ш x В)')),
                ('subtitle', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.type', verbose_name='Вид')),
                ('supports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icistore.supports', verbose_name='Опоры')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='MainPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='2023/10/18', verbose_name='Видео')),
                ('videoImage', models.ImageField(blank=True, null=True, upload_to='2023/10/18', verbose_name='Картинка Видео')),
                ('advantages', models.ManyToManyField(to='icistore.advantage', verbose_name='Преимущества')),
            ],
            options={
                'verbose_name': 'Видео для главной страницы',
                'verbose_name_plural': 'Видео для главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Legs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Материал изделия')),
                ('category', models.ManyToManyField(blank=True, to='icistore.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Материал изделия',
                'verbose_name_plural': 'Материал изделия',
            },
        ),
        migrations.AddField(
            model_name='armrests',
            name='category',
            field=models.ManyToManyField(blank=True, to='icistore.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='appearance',
            name='category',
            field=models.ManyToManyField(blank=True, to='icistore.category', verbose_name='Категория'),
        ),
    ]
