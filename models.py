from django.db import models
from django.contrib.auth.models import AbstractUser
from pgtrigger import *

# class UserAdmin(AbstractUser):
#     is_moder = models.BooleanField(blank=True, default=False)
#     is_ = models.BooleanField(blank=True, default=False)

class Role(models.Model):
    rolename = models.CharField(max_length=25, null=False, unique=True, db_index=True)
    def __str__(self):
        return self.rolename

class StatusPayment(models.Model):
    statusPaymentName = models.CharField(max_length=50, null=False, unique=True, db_index=True)
    def __str__(self):
        return self.statusPaymentName
    
class StatusOrder(models.Model):
    statusOrderName = models.CharField(max_length=50, null=False, unique=True, db_index=True)
    def __str__(self):
        return self.statusOrderName

class PaymentMethod(models.Model):
    paymentMethodName = models.CharField(null=False, unique=True)
    def __str__(self):
        return self.paymentMethodName
    
class Quality(models.Model):
    qualityName = models.CharField(null=False, unique=True)
    def __str__(self):
        return self.qualityName
    
class Rarity(models.Model):
    rarityName = models.CharField(null=False, unique=True)
    def __str__(self):
        return self.rarityName
        
class ItemType(models.Model):
    itemTypeName = models.CharField(null=False, unique=True)
    def __str__(self):
        return self.itemTypeName
    
class Category(models.Model):
    categoryName = models.CharField(null=False, unique=True)
    localizedName = models.CharField(null=False, unique=True)
    def __str__(self):
        return self.categoryName
    
class Tag(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tagName = models.CharField(null=False, unique=True)
    lozalizedName = models.CharField(null=False, unique=True)
    def __str__(self):
        return self.categoryName
    
class Item(models.Model):
    assetid = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    name_color = models.CharField(max_length=255, null=True, blank=True)
    name_on_market = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    quality = models.ForeignKey(Quality, on_delete=models.PROTECT, db_index=True, null=False)
    rarity = models.ForeignKey(Rarity, on_delete=models.PROTECT, db_index=True, null=False)
    isStattrak = models.BooleanField(default=False, null=False)
    stattrak_stat = models.IntegerField(null=True, blank=True)
    isTradable = models.BooleanField(default=True, null=False)
    isMarketable= models.BooleanField(default=True, null=False)
    type = models.ForeignKey(ItemType, on_delete=models.PROTECT, db_index=True, null=False)

    def __str__(self):
        #return self.get_pk()
        return f"{self.get_pk()} {self.name}"

class ItemTag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, db_index=True)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        #return self.get_pk()
        return f"{self.get_pk()} {self.item} | {self.tag}"

class Assortment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, db_index=True, null=False)
    quantity = models.IntegerField(default=0, null=False)
    isInStock = models.BooleanField(default=True)

    def __str__(self):
        #return self.get_pk()
        return f"{self.get_pk()} {self.item} | {self.quantity}"


class User(models.Model):
    login = models.CharField(max_length=25, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    nickname = models.CharField(max_length=25, blank=True, null=False)
    email = models.EmailField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=2, blank=True, null=False)
    balance = models.FloatField(blank=True, default=0)
    steamid = models.CharField(max_length=255, blank=True, null=True)
    steam_profile_url = models.CharField(max_length=255, blank=True, null=True)
    steam_avatar_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        index_together = ["login", "password", "nickname"]
        triggers = [
            SoftDelete(name='user', field='is_active')
        ]

    def __str__(self):
        return self.login


class Order(models.Model):
    statusOrder = models.ForeignKey(StatusOrder, on_delete=models.PROTECT, db_index=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    def get_pk(self):
        return str(self.pk)
    
    def __str__(self):
        return self.get_pk()

class Transactions(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, db_index=True)
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, db_index=True)
    statusPayment = models.ForeignKey(StatusPayment, on_delete=models.PROTECT, db_index=True)
    def get_pk(self):
        return str(self.pk)
    
    def __str__(self):
        return self.get_pk()

class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, db_index=True, null=False)
    item = models.ForeignKey(Item, on_delete=models.PROTECT, db_index=True, null=False)
    def get_pk(self):
        return str(self.pk)
    
    def __str__(self):
        #return self.get_pk()
        return f"{self.get_pk()} {self.item} | {self.order}"

