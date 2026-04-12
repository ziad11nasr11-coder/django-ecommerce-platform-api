from django.contrib import admin

# Register your models here.
from .models import User, AdminProfile, SellerProfile, CustomerProfile
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'phone')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('user_type',)


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'permissions_level', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('permissions_level',)

@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)

