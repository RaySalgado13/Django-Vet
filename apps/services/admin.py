from django.contrib import admin
from .models import Service, ServiceCategory, ServiceImage

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(ServiceImage)