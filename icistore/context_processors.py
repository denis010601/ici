from .models import Category  # Замените "myapp" на имя вашего приложения

def categories(request):
    categories_list = Category.objects.all()  # Получаем список категорий
    return {'categories': categories_list}