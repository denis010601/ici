from django.shortcuts import render, get_list_or_404
from .models import MainPageContent, Product, Category
# Create your views here.
def icihome(request):
    allCategory = Category.objects.all()
    allproduct = Product.objects.filter(is_top_product=True)[:5]
    content = MainPageContent.objects.get()
    return render(request, 'icistore/home.html', context={'content' : content, 'allproduct':allproduct, 'allCategory': allCategory})

def icistore(request, category_name):
    category = Category.objects.filter(name=category_name)
    allproduct = Product.objects.filter(category=category[0].id)
    print(allproduct[0].filters.all())
    return render(request, 'icistore/store.html' , context={'allproduct' : allproduct })

def icidetail(request, store_id):
    # store = get_object_or_404(Store, pk=store_id)
    return render(request, 'icistore/detail.html')