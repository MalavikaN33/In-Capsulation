from django.db import models


category_choice = (
        ('Furniture', 'Furniture'),
        ('IT Equipment', 'IT Equipment'),
        ('Phone', 'Phone'),
    )
class Category(models.Model):
    name= models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name




class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=False, null=False)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    #date = models.DateTimeField(auto_now_add=False, auto_now=False)

    #export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name +" "+ str(self.quantity)

# Create your models here.
class StockHistory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

class supplier (models.Model):
    supplier_name= models.CharField(max_length=50, blank=True, null=True)
    supplier_business= models.CharField(max_length=50, blank=True, null=True)
    supplier_email= models.CharField(max_length=50, blank=True, null=True)
    due_date=models.CharField(max_length=50, blank=True, null=True)
    amount=models.IntegerField(default='0', blank=True, null=True)
    status= models.CharField(max_length=50, blank=True, null=True)

class Userinfo(models.Model):
    username = models.CharField(max_length=30, null=True)
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    business = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

