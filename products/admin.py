from adminsortable.admin import SortableAdmin
from django.contrib import admin

from .models import Brand, Category, Facility, Industry, Photo, Product, Series, Tag


# Register your models here.
class CategoryAdmin(SortableAdmin):
    pass


class TagAdmin(SortableAdmin):
    pass


class IndustryAdmin(SortableAdmin):
    pass


class FacilityAdmin(SortableAdmin):
    pass


class BrandAdmin(SortableAdmin):
    pass


class SeriesAdmin(SortableAdmin):
    pass


class PhotoInline(admin.StackedInline):
    model = Photo


class ProductAdmin(SortableAdmin):
    inlines = [PhotoInline]
    prepopulated_fields = {"slug": ("markcode",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Product, ProductAdmin)
