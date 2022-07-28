from django.db import models
from apps.home.models import Customer

# Create your models here.
img_path = 'static/assets/media/services/'

class ServiceImage(models.Model):
    image = models.ImageField(upload_to=f'{img_path}ServiceImages')

    def __str__(self):
        return self.image

class ServiceCategory(models.Model):
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to=f'{img_path}ServiceCategories')
    
    def __str__(self):
        return self.category
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    images = models.ManyToManyField(ServiceImage)
    category = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class ScheduledService(models.Model):
    service = models.OneToOneField(Service, on_delete=models.PROTECT)
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT)
    date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.service[0:10]} - {self.customer[0:10]}'
    