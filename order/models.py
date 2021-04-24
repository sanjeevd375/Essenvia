from django.db import models
from datetime import datetime

# Create your models here.
class Order(models.Model):
    order_no = models.CharField(max_length=50, blank=True)
    order_details = models.TextField()
    order_time = models.DateTimeField(default=datetime.now)
    customer_details = models.TextField()
    delivery_dist = models.IntegerField()
    delivery_eta = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.order_no

    def generate_order_no(self):
        if not self.order_no:
            self.order_no = datetime.today().strftime('%d%m%Y') + "_" + str(self.pk)

    def save(self, *args, **kwargs):
        self.generate_order_no()
        super(Order, self).save(*args, **kwargs)
    