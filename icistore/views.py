from django.db.models import Q
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import MainPageContent, Product, Category
# Create your views here.
from .forms import ProductFilterForm
def icihome(request):
    if MainPageContent.objects.all() and Category.objects.all():
        allCategory = Category.objects.all()
        allproduct = Product.objects.filter(is_top_product=True)[:5]
        content = MainPageContent.objects.get()
        return render(request, 'icistore/home.html',context={'content': content, 'allproduct': allproduct, 'allCategory': allCategory})
    elif Category.objects.all() :
        allCategory = Category.objects.all()
        allproduct = Product.objects.filter(is_top_product=True)[:5]

        return render(request, 'icistore/home.html',context={'allproduct': allproduct, 'allCategory': allCategory})
    elif MainPageContent.objects.all():
        content = MainPageContent.objects.get()
        return render(request, 'icistore/home.html',context={'content': content})
    else:

        return render(request, 'icistore/home.html')

def icistore(request, category_name):
    category = Category.objects.filter(name=category_name).first()  # Get the category

    # Get the filter form
    filter_form = ProductFilterForm(request.POST or None, category=category)

    # Filter products based on the category and form choices
    products = Product.objects.filter(category=category)

    if filter_form.is_valid():
        size_filter = filter_form.cleaned_data.get('size')
        sleeper_ids = filter_form.cleaned_data.get('sleeper')
        appearance_ids = filter_form.cleaned_data.get('appearance')
        supports_ids = filter_form.cleaned_data.get('supports')
        armrests_ids = filter_form.cleaned_data.get('armrests')

        q_objects = Q()

        if size_filter == 'small':
            q_objects &= Q(size__sizeL__lte=2000)
        elif size_filter == 'medium':
            q_objects &= Q(size__sizeL__range=(2000, 3000))
        elif size_filter == 'large':
            q_objects &= Q(size__sizeL__gt=3000)

        if sleeper_ids:
            q_objects &= Q(has_sleeper__in=sleeper_ids)

        if appearance_ids:
            q_objects &= Q(appearance__in=appearance_ids)

        if supports_ids:
            q_objects &= Q(supports__in=supports_ids)

        if armrests_ids:
            q_objects &= Q(armrests__in=armrests_ids)

        products = products.filter(q_objects)

    return render(request, 'icistore/store.html', context={'products': products, 'form': filter_form})

def icidetail(request, category_name ,product_name):
    product = get_object_or_404(Product, title=product_name)
    all_products = Product.objects.filter(subtitle=product.subtitle, category=product.category)
    

    data_dict = {
        'form': {
            'verbose_name': product._meta.get_field('form').verbose_name,
            'value': product.form
        },
        'size': {
            'verbose_name': product._meta.get_field('size').verbose_name,
            'value': product.size
        },
        'has_sleeper': {
            'verbose_name': product._meta.get_field('has_sleeper').verbose_name,
            'value': product.has_sleeper
        },
        'appearance': {
            'verbose_name': product._meta.get_field('appearance').verbose_name,
            'value': product.appearance
        },
        'supports': {
            'verbose_name': product._meta.get_field('supports').verbose_name,
            'value': product.supports
        },
        'armrests': {
            'verbose_name': product._meta.get_field('armrests').verbose_name,
            'value': product.armrests
        }
    }
   
    context = {
        'product': product,

        'data_dict' : data_dict
    }
    if len(all_products) > 1:
        context['allproducts'] = all_products
    print(context)
    return render(request, 'icistore/detail.html', context=context)