from adminsortable.models import SortableMixin
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

# from ordered_model.models import OrderedModel


# Create your models here.
class Category(MPTTModel, SortableMixin):
    title = models.CharField(max_length=255, db_index=True, verbose_name="カテゴリー名（日本語）")
    title_en = models.CharField(max_length=255, db_index=True, verbose_name="カテゴリー（英語）")
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", blank=True)
    photo = ThumbnailerImageField(upload_to="photos", blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    parent = TreeForeignKey(
        "self", related_name="child", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_list_by_category", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ["the_order"]


class Tag(SortableMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["the_order"]


class Facility(SortableMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["the_order"]


class Industry(SortableMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", blank=True)
    photo = ThumbnailerImageField(upload_to="photos", blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["the_order"]


class Brand(SortableMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Brand, self).save(*args, **kwargs)

    class Meta:
        ordering = ["the_order"]


class Series(SortableMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Series, self).save(*args, **kwargs)

    class Meta:
        ordering = ["the_order"]


class Product(TimeStampedModel, SortableMixin):
    title = models.CharField(max_length=255, null=False, blank=False)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    markcode = models.PositiveIntegerField(null=False, blank=False)
    pos = models.BigIntegerField(null=True, blank=True)
    gtin = models.BigIntegerField(null=True, blank=True)
    packing = models.CharField(max_length=255, null=True, blank=True)
    packing_weight = models.CharField(max_length=100, null=True, blank=True)
    packing_width = models.CharField(max_length=100, null=True, blank=True)
    packing_height = models.CharField(max_length=100, null=True, blank=True)
    packing_depth = models.CharField(max_length=100, null=True, blank=True)
    carton_weight = models.CharField(max_length=100, null=True, blank=True)
    carton_width = models.CharField(max_length=100, null=True, blank=True)
    carton_height = models.CharField(max_length=100, null=True, blank=True)
    carton_depth = models.CharField(max_length=100, null=True, blank=True)
    expiration_date = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField(default=0, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    caution = models.TextField(null=True, blank=True)
    additive = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    shipping_date = models.DateTimeField(null=True, blank=True)
    hero = ThumbnailerImageField(upload_to="photos/heros/", null=True, blank=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    series = models.ForeignKey(Series, null=True, blank=True, on_delete=models.SET_NULL)
    handling_water = models.TextField(blank=True, null=True)
    handling_time = models.TextField(blank=True, null=True)
    handling_temp = models.TextField(blank=True, null=True)
    handling_recipe = models.TextField(blank=True, null=True)
    handling_extra = models.TextField(blank=True, null=True)
    handling_link = models.CharField(max_length=255, null=True, blank=True)
    freespace_a = models.TextField(null=True, blank=True)
    freespace_b = models.TextField(null=True, blank=True)
    freespace_c = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    related = models.ManyToManyField("self", null=True, blank=True, symmetrical=False)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    category = models.ManyToManyField(
        Category,
        related_name="product",
        blank=True,
    )
    tag = models.ManyToManyField(
        Tag,
        related_name="product",
        blank=True,
    )
    industry = models.ManyToManyField(
        Industry,
        related_name="product",
        blank=True,
    )
    facility = models.ManyToManyField(
        Facility,
        related_name="product",
        blank=True,
    )

    def __str__(self):
        return self.title + " (" + str(self.markcode) + ")"

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.markcode)
        return super(Product, self).save(*args, **kwargs)

    def main_category(self):
        return self.category.get(parent_id__isnull=True)

    def main_photo(self):
        return self.photos.get(label="main")

    def preservation(self):
        for tag in self.tag.all():
            if tag.slug == "dry" or tag.slug == "frozen":
                return tag

    class Meta:
        ordering = ["the_order"]


class Photo(models.Model):
    LABEL = Choices("main", "cooked", "package")

    photo = ThumbnailerImageField(upload_to="photos", blank=False)
    product = models.ForeignKey(
        Product, related_name="photos", on_delete=models.CASCADE
    )
    label = StatusField(choices_name="LABEL", default=LABEL.cooked)
