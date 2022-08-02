from adminsortable.admin import SortableAdmin, SortableTabularInline
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe
from import_export.admin import ExportActionMixin

from .models import (
    Category,
    Ingredient,
    Instruction,
    Nutrient,
    Photo,
    Recipe,
    RecipeNutrient,
    RecipeProduct,
    RecommendedItem,
    Tag,
)


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>'
            )

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe("".join(output))


# Register your models here.
class CategoryAdmin(ExportActionMixin, SortableAdmin):
    list_display = ("title", "title_en", "subtitle", "slug", "show_in_menu", "parent")


class TagAdmin(ExportActionMixin, SortableAdmin):
    pass


class NutrientAdmin(ExportActionMixin, admin.ModelAdmin):
    pass


class RecommendedItemAdmin(ExportActionMixin, admin.ModelAdmin):
    pass


class RecipeProductInline(SortableTabularInline):
    autocomplete_fields = ["product"]
    model = RecipeProduct
    extra = 1


class RecipeNutrientInline(SortableTabularInline):
    model = RecipeNutrient
    extra = 1


class IngredientInline(SortableTabularInline):
    model = Ingredient
    extra = 1


class InstructionInline(SortableTabularInline):
    model = Instruction
    extra = 1


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    formfield_overrides = {models.ImageField: {"widget": AdminImageWidget}}


class RecipeAdmin(ExportActionMixin, SortableAdmin):
    list_display = ("title", "slug", "is_new", "is_published")
    # list_editable = ( "title", )
    search_fields = ["title", "slug", "code"]
    readonly_fields = ("code",)
    filter_horizontal = (
        "related",
        "sub_recipe",
        "category",
        "tag",
    )
    inlines = (
        RecipeProductInline,
        IngredientInline,
        InstructionInline,
        RecipeNutrientInline,
        PhotoInline,
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Nutrient, NutrientAdmin)
admin.site.register(RecommendedItem, RecommendedItemAdmin)
admin.site.register(Recipe, RecipeAdmin)
