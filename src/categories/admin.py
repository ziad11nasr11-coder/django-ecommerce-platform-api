from django.contrib import admin
from .models import (
    Department,
    Category,
    CategoryAttribute,
    CategoryAttributeOption
)
from mptt.admin import MPTTModelAdmin

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ("name", "department", "parent", "is_active")
    list_filter = ("department", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(CategoryAttribute)
class CategoryAttributeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "attr_type", "is_required", "is_filterable")
    list_filter = ("attr_type", "is_filterable")
    prepopulated_fields = {"slug": ("name",)}

