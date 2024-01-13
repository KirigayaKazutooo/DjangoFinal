from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Supplier(models.Model):
    SUPPLIER_ID = models.AutoField(primary_key=True)
    SUPPLIER_NAME = models.CharField(max_length=100)
    SUPPLIER_ADDRESS = models.CharField(max_length=200)
    SUPPLIER_PHONE = models.CharField(max_length=12)
    def __str__(self):
        return self.SUPPLIER_NAME
    
class Product(models.Model):
    PROD_NAME = models.CharField(max_length=100)
    PROD_DESCRIPTION = models.CharField(max_length=200)
    #PROD_DATE_POSTED = models.DateTimeField(default = timezone.now)
    PROD_IMAGE = models.ImageField(default='default.png', upload_to='product_pics')
    PROD_QUANTITY = models.IntegerField(default=0)
    PROD_PRICE = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    awaiting_approval = models.BooleanField(default=False)

    def __str__(self):
        return self.PROD_NAME
    
    def save(self, *args, **kwargs):
        if self.PROD_PRICE is not None and self.PROD_PRICE < 0:
            self.PROD_PRICE = abs(self.PROD_PRICE)
        if self.PROD_QUANTITY is not None and self.PROD_QUANTITY < 0:
            self.PROD_QUANTITY = abs(self.PROD_QUANTITY)
        super().save(*args, **kwargs)
        
        img = Image.open(self.PROD_IMAGE.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.PROD_IMAGE.path)
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
    
    
class PurchaseOrder(models.Model):
    ORD_EMPLOYEE = models.CharField(max_length=100)
    ORD_DATE_POSTED = models.DateTimeField(default=timezone.now)
    ORD_NAME = models.CharField(max_length=200)
    ORD_QUANTITY = models.IntegerField(default=0)
    ORD_PRICE = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    ORD_DESCRIPTION = models.CharField(max_length=200)
    
    APPROVED = 'Approved'
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    def __str__(self):
        return self.ORD_NAME 

class Cart(models.Model):
    CART_ID = models.AutoField(primary_key=True)
    CART_QUANTITY = models.IntegerField(default=0)
    CART_DATE_ADDED = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart ID: {self.cart_id} - Product: {self.product.PROD_NAME}"




class RequestedProduct(models.Model):
    REQ_PROD_ID = models.AutoField(primary_key=True)
    REQ_PROD_QUANTITY = models.IntegerField(default=0)
    REQ_PROD_DATE_ADDED = models.DateTimeField(default=timezone.now)
    REQ_PROD_NAME = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"REQ_PROD ID: {self.REQ_PROD_ID} - Product: {self.product.PROD_NAME}"

class Requisition(models.Model):
    REQ_ID = models.AutoField(primary_key=True)
    REQ_NAME = models.CharField(max_length=100)
    REQ_QUANTITY = models.CharField(max_length=100, default=0)
    REQ_DESCRIPTION = models.CharField(max_length=200, default='')
    REQ_EMPLOYEE = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    APPROVED = 'Approved'
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    
    requested_product = models.ForeignKey(RequestedProduct, on_delete=models.CASCADE)

    @property
    def REQ_STATUS(self):
        return self.status

