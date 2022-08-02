from random import randrange

from adminsortable.models import SortableMixin
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

from products.models import Brand, Product, Series

# Create your models here.


def unique_rand():
    for _ in range(100):
        new_code = ""
        charset = "0123456789"
        for i in range(8):
            new_code += charset[randrange(0, len(charset))]
        if not Recipe.objects.filter(code=new_code).exists():
            return new_code
    raise ValueError("Too many attempts to generate the code")


class Category(MPTTModel, SortableMixin):
    title = models.CharField(max_length=255, db_index=True, verbose_name="カテゴリー名（日本語）")
    title_en = models.CharField(max_length=255, db_index=True, verbose_name="カテゴリー（英語）")
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", blank=True)
    photo = ThumbnailerImageField(upload_to="photos", blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    show_in_menu = models.BooleanField(default=False)
    parent = TreeForeignKey(
        "self", related_name="child", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        if self.parent:
            return self.title + " (" + str(self.parent) + ")"
        else:
            return self.title

    def get_absolute_url(self):
        return reverse("recipe_list_by_category", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ["the_order"]


class Tag(SortableMixin):
    LABEL = Choices(
        ("tag", "ノーマルタグ"),
        ("menu", "メニュータイプ"),
        ("dish", "ディッシュタイプ"),
        ("business", "業態"),
        ("event", "イベント"),
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    label = StatusField(choices_name="LABEL", default=LABEL.tag)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["the_order"]


class Nutrient(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Recipe(TimeStampedModel, SortableMixin):
    title = models.CharField(max_length=255, null=False, blank=False)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    code = models.SlugField(max_length=8, unique=True, default=unique_rand)
    slug = models.SlugField(max_length=30, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    serves = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    is_new = models.BooleanField(default=True)
    is_searchable = models.BooleanField(default=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", null=True, blank=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    series = models.ForeignKey(Series, null=True, blank=True, on_delete=models.SET_NULL)
    sub_recipe = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="recipe_owner",
    )
    related = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="recipe_relative",
    )
    caution = models.TextField(null=True, blank=True)
    freespace_a = models.TextField(null=True, blank=True)
    freespace_b = models.TextField(null=True, blank=True)
    freespace_c = models.TextField(null=True, blank=True)
    freespace_d = models.TextField(null=True, blank=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    category = models.ManyToManyField(
        Category,
        related_name="recipe",
        blank=True,
    )
    tag = models.ManyToManyField(
        Tag,
        related_name="recipe",
        blank=True,
    )
    products = models.ManyToManyField(
        Product,
        related_name="recipe",
        blank=True,
        through="RecipeProduct",
    )
    nutrients = models.ManyToManyField(
        Nutrient,
        related_name="recipe",
        blank=True,
        through="RecipeNutrient",
    )

    def __str__(self):
        return self.title + " (" + str(self.slug) + ")"

    def main_category(self):
        return self.category.filter(show_in_menu=True).first()

    def main_photo(self):
        return self.photos.get(label="main")

    def menu_types(self):
        return self.tag.filter(label="menu")

    def dish_types(self):
        return self.tag.filter(label="dish")

    def events(self):
        return self.tag.filter(label="event")

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.code)
        return super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ["the_order"]


class Ingredient(SortableMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    amount = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE
    )
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["the_order"]


class Instruction(SortableMixin):
    LABEL = Choices(("step", "ステップ"), ("title", "タイトル"))
    step = models.TextField(null=True, blank=True)
    recipe = models.ForeignKey(
        Recipe, related_name="instructions", on_delete=models.CASCADE
    )
    label = StatusField(choices_name="LABEL", default=LABEL.step)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["the_order"]


class Photo(models.Model):
    LABEL = Choices("main", "cooked", "package")
    photo = ThumbnailerImageField(upload_to="photos", blank=False)
    recipe = models.ForeignKey(Recipe, related_name="photos", on_delete=models.CASCADE)
    label = StatusField(choices_name="LABEL", default=LABEL.main)


class RecipeProduct(SortableMixin):
    recipe = models.ForeignKey(
        Recipe, null=False, blank=False, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    amount = models.CharField(max_length=255, null=True, blank=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    show_in_list = models.BooleanField(default=True)

    class Meta:
        ordering = ["the_order"]


class RecipeNutrient(SortableMixin):
    recipe = models.ForeignKey(
        Recipe, null=False, blank=False, on_delete=models.CASCADE
    )
    nutrient = models.ForeignKey(
        Nutrient, null=False, blank=False, on_delete=models.CASCADE
    )
    amount = models.CharField(max_length=255, null=False, blank=False)
    label = models.CharField(max_length=255, null=True, blank=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["the_order"]


class RecommendedItem(SortableMixin):
    recipe = models.ForeignKey(
        Recipe, null=False, blank=False, on_delete=models.CASCADE
    )
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.recipe.title

    class Meta:
        ordering = ["the_order"]
