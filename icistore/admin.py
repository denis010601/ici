from django.contrib import admin
from django.utils.html import format_html

from imagekit.admin import AdminThumbnail

from .models import Category, Sofa, InteriorSofa, Chair, Ottoman, SofaFilter, InteriorSofaFilter, ChairFilter, \
    OttomanFilter, Material, ImageModel, Gallery


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']



class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SofaFilterInline(admin.TabularInline):
    model = SofaFilter
    extra = 1


class InteriorSofaFilterInline(admin.TabularInline):
    model = InteriorSofaFilter
    extra = 1


class ChairFilterInline(admin.TabularInline):
    model = ChairFilter
    extra = 1


class OttomanFilterInline(admin.TabularInline):
    model = OttomanFilter
    extra = 1


class SofaAdmin(admin.ModelAdmin):
    inlines = [SofaFilterInline]
    list_display = ('title', 'category', 'is_published', 'is_top_product')


class InteriorSofaAdmin(admin.ModelAdmin):
    inlines = [InteriorSofaFilterInline]
    list_display = ('title', 'category', 'is_published', 'is_top_product')


class ChairAdmin(admin.ModelAdmin):
    inlines = [ChairFilterInline]
    list_display = ('title', 'category', 'is_published', 'is_top_product')


class OttomanAdmin(admin.ModelAdmin):
    inlines = [OttomanFilterInline]
    list_display = ('title', 'category', 'is_published', 'is_top_product')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" style="height:100px;width:100px;"/>'.format(obj.image.url))

    display_image.short_description = 'Image'

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ImageModel, ImageModelAdmin)
admin.site.register(Sofa, SofaAdmin)
admin.site.register(InteriorSofa, InteriorSofaAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Ottoman, OttomanAdmin)
admin.site.register(Category)
admin.site.register(Material, MaterialAdmin)
