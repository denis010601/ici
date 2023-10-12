from django.urls import path
from .views import *
urlpatterns = [
    path('', icihome, name="home"),
    path('store/<int:category_id>', icistore, name="store"),
    path('store/<int:store_id>', icidetail, name="detail"),
]