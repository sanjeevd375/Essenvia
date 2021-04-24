from django.db import models
from datetime import datetime

# Create your models here.
class Inventory(models.Model):
    CATEGORY_CHOICES = (
        ('television', 'Television'),
        ('refrigerator', 'Female'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    model_no = models.CharField(max_length=50, unique=True)
    availability_count = models.IntegerField()
    price = models.IntegerField()
    added_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.model_no + self.category

    def check_item_availability(data=None):
        available = True
        message = 'OK'
        for product in data['items']:
            item = Inventory.objects.get(model_no=product['model_no'])
            if item.availability_count >= product['count']:
                pass
            else:
                 available = False
                 message = item.model_no + "stock availability is : "+ str(product['count']-item.availability_count)

                 return available, message

        #Updating Inventory Products
        for product in data['items']:
            item = Inventory.objects.get(model_no=product['model_no'])
            item.availability_count -= product['count']
            item.save()

        return available, message
                    

