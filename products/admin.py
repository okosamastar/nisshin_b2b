from django.contrib import admin

from .models import Category, Facility, Industry, Photo, Product, Tag


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class IndustryAdmin(admin.ModelAdmin):
    pass


class FacilityAdmin(admin.ModelAdmin):
    pass


class PhotoInline(admin.StackedInline):
    model = Photo


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Product, ProductAdmin)
