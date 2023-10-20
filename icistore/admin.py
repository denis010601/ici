from django.contrib import admin

from .models import *


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SofaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_top_product')


class InteriorSofaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_top_product')


class ChairAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_top_product')


class OttomanAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_top_product')
class MainPageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Проверка, есть ли уже запись
        return not MainPageContent.objects.exists()

admin.site.register(MainPageContent, MainPageContentAdmin)
admin.site.register(Type)
admin.site.register(Advantage)
admin.site.register(Category)
admin.site.register(Material, MaterialAdmin)

admin.site.register(ImageModel, ImageModelAdmin)
admin.site.register(FormProduct)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Sleeper)
admin.site.register(Appearance)
admin.site.register(Legs)