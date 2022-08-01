from adminsortable.admin import SortableAdmin, SortableTabularInline
from django.contrib import admin
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
    Tag,
)


# Register your models here.
class CategoryAdmin(ExportActionMixin, SortableAdmin):
    pass


class TagAdmin(ExportActionMixin, SortableAdmin):
    pass


class NutrientAdmin(ExportActionMixin, admin.ModelAdmin):
    pass


class RecipeProductInline(SortableTabularInline):
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


class RecipeAdmin(ExportActionMixin, SortableAdmin):
    readonly_fields = ("code",)
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
admin.site.register(Recipe, RecipeAdmin)
