from datetime import datetime

from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from model_utils import Choices
from model_utils.fields import StatusField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name="カテゴリー")
    description = models.TextField(blank=True, null=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", blank=True)
    photo = ThumbnailerImageField(upload_to="photos", blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey(
        "self", related_name="child", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("product_list_by_category", args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)


class Facility(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", blank=True)
    photo = ThumbnailerImageField(upload_to="photos", blank=True)
    slug = models.SlugField(max_length=100, unique=True)


class Product(models.Model):

    PRESERVATION = Choices(
        ("room_temp", "常温"),
        ("frozen", "冷凍"),
    )

    title = models.CharField(max_length=255, null=False, blank=False)
    subtitle = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    shipping_date = models.DateTimeField(blank=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", blank=True)
    preservation = StatusField(
        choices_name="PRESERVATION", help_text="温度帯", default=PRESERVATION.room_temp
    )
    category = models.ManyToManyField(
        Category,
        related_name="product",
        default=False,
        blank=True,
    )
    tag = models.ManyToManyField(
        Tag,
        related_name="product",
        default=False,
        blank=True,
    )
    industry = models.ManyToManyField(
        Industry,
        related_name="product",
        default=False,
        blank=True,
    )
    facility = models.ManyToManyField(
        Facility,
        related_name="product",
        default=False,
        blank=True,
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    LABEL = Choices("main", "cooked", "package")

    photo = ThumbnailerImageField(upload_to="photos", blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    label = StatusField(choices_name="LABEL", default=LABEL.cooked)


class Series(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Brand(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)


class Handling(models.Model):
    water = models.CharField(max_length=255, null=False, blank=False)
    time = models.CharField(max_length=255, null=False, blank=False)
    temperature = models.CharField(max_length=255, null=False, blank=False)
    recipe = models.CharField(max_length=255, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
