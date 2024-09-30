from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATE_CHOICE=(
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Bihar','Bihar'),
    ('Gujrat','Gujrat'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Haryana','Haryana'),
    ('Rajasthan','Rajasthan'),
    ('Maharashtra','Maharashtra'),
    
)

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    cat_img=models.ImageField(upload_to="category_img")

    def __str__(self):
        return self.category_name
    
class Brand_name(models.Model):
    brand_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    name=models.CharField(max_length=300)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    date_createtime=models.DateField(auto_now_add=True)
    date_updatetime=models.DateField(auto_now=True)
    image=models.ImageField(upload_to="Prodect_img")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand_name, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    locality=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    mobile=models.IntegerField(default=0)
    pincode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=200)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICE=(
        ('Accepted','Accepted'),
        ('Packed','Packed'),
        ('On the Way','On the Way'),
        ('Delivered','Delivered'),
        ('Cancel','Cancel'),
        ('Pending','Pending')
    )

class Payment(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        amount=models.FloatField()
        razorpay_order_id=models.CharField(max_length=200,blank=True,null=True)
        razorpay_payment_status=models.CharField(max_length=200,blank=True,null=True)
        razorpay_payment_id=models.CharField(max_length=200,blank=True,null=True)
        paid=models.BooleanField(default=False)


class PlacedOrder(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
        product=models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity=models.PositiveIntegerField(default=1)
        ordered_date=models.DateTimeField(auto_now_add=True)
        status=models.CharField(max_length=100, choices=STATUS_CHOICE, default='Pending')
        payment=models.ForeignKey(Payment, on_delete=models.CASCADE, default='')

        @property
        def total_cost(self):
             return self.quantity * self.product.discounted_price
        

class ContactUs(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     name=models.CharField(max_length=200)
     email=models.CharField(max_length=200)
     number=models.IntegerField(default=0)
     subject=models.CharField(max_length=250)
     message=models.TextField()

     def __str__(self):
          return self.name