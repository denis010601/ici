from django.contrib import admin

from .models import Category, Sofa, InteriorSofa, Chair, Ottoman, Material, ImageModel


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


admin.site.register(Category)
admin.site.register(Material, MaterialAdmin)

admin.site.register(ImageModel, ImageModelAdmin)

admin.site.register(Sofa, SofaAdmin)
admin.site.register(InteriorSofa, InteriorSofaAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Ottoman, OttomanAdmin)
