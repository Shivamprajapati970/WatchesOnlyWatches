from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','selling_price','discounted_price','category','brand')
    list_filter=('category','brand')
    search_fields=('name',)


@admin.register(Customer)
class CustomerAdimn(admin.ModelAdmin):
    list_display=('id','user','locality','city','state','pincode')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('id','user','product','quantity')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(PlacedOrder)
class PlacedOrderAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['id','name','email','number','subject','message']

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand_name)
admin.site.register(Category)
