from adminsortable.admin import SortableAdmin
from django.contrib import admin

from .models import Brand, Category, Facility, Industry, Photo, Product, Series, Tag


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(SortableAdmin):
    pass


class IndustryAdmin(admin.ModelAdmin):
    pass


class FacilityAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


class SeriesAdmin(admin.ModelAdmin):
    pass


class PhotoInline(admin.StackedInline):
    model = Photo


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    prepopulated_fields = {"slug": ("markcode",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Product, ProductAdmin)
