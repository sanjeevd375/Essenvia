from django.db import models
from datetime import datetime
import random

# Create your models here.
class Order(models.Model):
    ORDER_STATUS = (
        ('confirmed', 'CONFIRMED'),
        ('processing', 'PROCESSING'),
        ('in-transit','IN-TRANSIT'),
        ('delivered','DELIVERED')
    )
    order_no = models.CharField(max_length=50, unique=True, blank=True)
    order_details = models.TextField()
    order_time = models.DateTimeField(default=datetime.now)
    customer_details = models.TextField()
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='confirmed')
    delivery_dist = models.IntegerField()
    delivery_eta = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.order_no

    def generate_order_no(self):
        if not self.order_no:
            self.order_no = datetime.today().strftime('%d%m%Y') + "_" + str(random.randint(0,999999))

    def save(self, *args, **kwargs):
        self.generate_order_no()
        super(Order, self).save(*args, **kwargs)
    