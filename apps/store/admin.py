from django.contrib import admin
from .models import Product,ProductCategory,ProductColor,ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
