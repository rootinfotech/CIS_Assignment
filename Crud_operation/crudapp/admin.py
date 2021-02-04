from django.contrib import admin
from . models import Category, Tags, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category, CategoryAdmin)

class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Tags, TagsAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'image', 'category', 'user', 'description']

admin.site.register(Product, ProductAdmin)