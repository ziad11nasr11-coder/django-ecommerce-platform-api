from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Department(models.Model):
    name        = models.CharField(max_length=200, unique=True)
    slug        = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Department"
        verbose_name_plural = "Departments"
        ordering            = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("categories:department-detail", kwargs={"slug": self.slug})

    def get_active_categories(self):
        return self.categories.filter(is_active=True, level=0)


class Category(MPTTModel):
    department  = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="categories",
    )
    parent      = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    name             = models.CharField(max_length=200)
    slug             = models.SlugField(max_length=220, blank=True)
    description      = models.TextField(blank=True)
    meta_title       = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    is_active        = models.BooleanField(default=True)
    is_featured      = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name        = "Category"
        verbose_name_plural = "Categories"
        unique_together     = [("department", "slug")]

    def __str__(self):
        ancestors = self.get_ancestors(include_self=True)
        return " > ".join([a.name for a in ancestors])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        if self.parent:
            self.department = self.parent.department
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("categories:category-detail", kwargs={
            "dept_slug": self.department.slug,
            "slug": self.slug,
        })

    @property
    def is_root_category(self):
        return self.is_root_node()

    @property
    def breadcrumb(self):
        return list(self.get_ancestors(include_self=True))

    def get_all_products(self):
        descendants = self.get_descendants(include_self=True)
        return self.department.products.filter(category__in=descendants)


class CategoryAttribute(models.Model):
    TYPE_CHOICES = [
        ("text",        "Text"),
        ("number",      "Number"),
        ("boolean",     "Boolean"),
        ("select",      "Select"),
        ("multiselect", "Multi-Select"),
        ("range",       "Range"),
    ]

    category      = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="attributes",
    )
    name          = models.CharField(max_length=100)
    slug          = models.SlugField(max_length=120, blank=True)
    attr_type     = models.CharField(max_length=20, choices=TYPE_CHOICES, default="text")
    unit          = models.CharField(max_length=30, blank=True)
    is_required   = models.BooleanField(default=False)
    is_filterable = models.BooleanField(default=True)

    class Meta:
        verbose_name        = "Category Attribute"
        verbose_name_plural = "Category Attributes"
        ordering            = ["name"]
        unique_together     = [("category", "slug")]

    def __str__(self):
        return f"{self.category.name} — {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class CategoryAttributeOption(models.Model):
    attribute = models.ForeignKey(
        CategoryAttribute,
        on_delete=models.CASCADE,
        related_name="options",
    )
    value = models.CharField(max_length=100)


    class Meta:
        verbose_name        = "Attribute Option"
        verbose_name_plural = "Attribute Options"
        ordering            = ["value"]
        unique_together     = [("attribute", "value")]

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"

