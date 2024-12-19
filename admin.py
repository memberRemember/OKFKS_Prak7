from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'nickname', 'email', 'role', 'is_active', 'date_created', 'balance', 'steamid', 'steam_profile_url', 'steam_avatar_url')
    model = User

    def rolename(self, obj):
        return obj.role.rolename

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('rolename',)

@admin.register(StatusOrder)
class StatusOrderAdmin(admin.ModelAdmin):
    list_display = ('statusOrderName',)

@admin.register(StatusPayment)
class StatusPaymentAdmin(admin.ModelAdmin):
    list_display = ('statusPaymentName',)

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('paymentMethodName',)

@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ('qualityName',)
    
@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ('rarityName',)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('category', 'tagName', 'lozalizedName',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('assetid', 'name', 'name_color', 'name_on_market', 'description', 'quality', 'rarity', 'isStattrak', 'stattrak_stat', 'isTradable', 'isMarketable', 'type',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('statusOrder', 'user', 'price',)

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('order', 'paymentMethod', 'statusPayment',)

@admin.register(Order_Item)
class Order_ItemAdmin(admin.ModelAdmin):
    list_display = ('order','item',)

@admin.register(Assortment)
class AssortmentAdmin(admin.ModelAdmin):
    list_display = ('item','quantity','isInStock',)

@admin.register(ItemTag)
class ItemTagAdmin(admin.ModelAdmin):
    list_display = ('item','tag',)

@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('itemTypeName',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName', 'localizedName',)
