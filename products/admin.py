from adminsortable.admin import SortableAdmin
from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import Brand, Category, Facility, Industry, Photo, Product, Series, Tag


# Register your models here.
class CategoryAdmin(ExportActionMixin, SortableAdmin):
    pass


class TagAdmin(ExportActionMixin, SortableAdmin):
    pass


class IndustryAdmin(ExportActionMixin, SortableAdmin):
    pass


class FacilityAdmin(ExportActionMixin, SortableAdmin):
    pass


class BrandAdmin(ExportActionMixin, SortableAdmin):
    pass


class SeriesAdmin(ExportActionMixin, SortableAdmin):
    pass


class PhotoInline(admin.StackedInline):
    model = Photo


class ProductAdmin(ExportActionMixin, SortableAdmin):
    list_display = ("title", "markcode", "brand", "series", "is_new", "is_published")
    search_fields = ["title", "markcode"]
    inlines = [PhotoInline]
    prepopulated_fields = {"slug": ("markcode",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Product, ProductAdmin)
