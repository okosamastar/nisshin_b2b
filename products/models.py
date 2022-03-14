from datetime import datetime

from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name="カテゴリー")
    description = models.TextField(blank=True, null=True)
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


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True)
    photo = ThumbnailerImageField(upload_to="photos", blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ManyToManyField(
        "Category",
        related_name="products",
        default=False,
        blank=True,
    )

    def __str__(self):
        return self.name
