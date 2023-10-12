from django.shortcuts import render, get_list_or_404

# Create your views here.
def icihome(request):
    return render(request, 'icistore/home.html')

def icistore(request):
    return render(request, 'icistore/store.html')

def icidetail(request, store_id):
    # store = get_object_or_404(Store, pk=store_id)
    return render(request, 'icistore/detail.html')