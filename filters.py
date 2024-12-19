from django_filters import rest_framework as filters
from .models import *

# class UserFilter(filters.FilterSet):
#     class Meta:
#         model = User
#         fields = ['login', 'password', 'nickname', 'email', 'date_created', 'is_active', 'role']


class UserModelFilter(filters.FilterSet):

    login = filters.CharFilter(field_name='login', lookup_expr='icontains')
    password = filters.CharFilter(field_name='password', lookup_expr='exact')
    nickname = filters.CharFilter(field_name='nickname', lookup_expr='icontains')
    balance = filters.CharFilter(field_name='balance', lookup_expr='icontains')
    steamid = filters.CharFilter(field_name='steamid', lookup_expr='icontains')

    created_after = filters.DateTimeFilter(field_name='date_created', lookup_expr='gte')
    created_before = filters.DateTimeFilter(field_name='date_created', lookup_expr='lte')
    
    class Meta:
        model = User
        fields = ['login', 'password', 'nickname', 'role', 'email', 'nickname', 'balance', 'steamid', 'steam_profile_url', 'steam_avatar_url', 'is_active',]

    

class RoleModelFilter(filters.FilterSet):
    rolename = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Role
        fields = ['rolename',]

class StatusPaymentModelFilter(filters.FilterSet):
    statusPaymentName = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StatusPayment
        fields = ['statusPaymentName',]

class StatusOrderModelFilter(filters.FilterSet):
    statusOrderName = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StatusOrder
        fields = ['statusOrderName',]

class PaymentMethodModelFilter(filters.FilterSet):
    paymentMethodName = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = PaymentMethod
        fields = ['paymentMethodName',]

class QualityModelFilter(filters.FilterSet):
    qualityName = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Quality
        fields = ['qualityName',]

class RarityModelFilter(filters.FilterSet):
    rarityName = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Rarity
        fields = ['rarityName',]
        
class ItemTypeModelFilter(filters.FilterSet):
    itemTypeName = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = ItemType
        fields = ['itemTypeName',]

class TagModelFilter(filters.FilterSet):
    category = filters.Filter(field_name='category_id', lookup_expr='exact')
    localizedName = filters.CharFilter(lookup_expr='icontains')
    tagName = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Tag
        fields = ['tagName', 'localizedName', 'category']

class CategoryModelFilter(filters.FilterSet):
    categoryName = filters.CharFilter(lookup_expr='icontains')
    localizedName = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Category
        fields = ['categoryName', 'localizedName',]


class ItemModelFilter(filters.FilterSet):
    assetid = filters.CharFilter(lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains')
    name_color = filters.CharFilter(lookup_expr='icontains')
    name_on_market = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    quality = filters.Filter(field_name='quality_id', lookup_expr='exact')
    rarity = filters.Filter(field_name='rarity_id', lookup_expr='exact')
    isStatTrak = filters.CharFilter(lookup_expr='icontains')
    stattrak_stat = filters.CharFilter(lookup_expr='icontains')
    isTradable = filters.CharFilter(lookup_expr='icontains')
    isMarketable = filters.CharFilter(lookup_expr='icontains')
    type = filters.Filter(field_name='type_id', lookup_expr='exact')
    
    class Meta:
        model = Item
        fields = ['assetid','name','name_color', 'name_on_market', 'description', 'quality', 'rarity', 'isStatTrak', 'stattrak_stat', 'isTradable', 'isMarketable', 'type']

class OrderModelFilter(filters.FilterSet):
    statusOrder = filters.Filter(field_name='statusOrder_id', lookup_expr='exact')
    user = filters.Filter(field_name='user_id', lookup_expr='exact')
    price = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Order
        fields = ['statusOrder','user','price']

class TransactionsModelFilter(filters.FilterSet):
    order = filters.Filter(field_name='order_id', lookup_expr='exact')
    paymentMethod = filters.Filter(field_name='paymentMethod_id', lookup_expr='exact')
    statusPayment = filters.Filter(field_name='statusPayment_id', lookup_expr='exact')
    
    class Meta:
        model = Transactions
        fields = ['order','paymentMethod','statusPayment']

class ItemTagModelFilter(filters.FilterSet):
    item = filters.Filter(field_name='item_id', lookup_expr='exact')
    tag = filters.Filter(field_name='tag_id', lookup_expr='exact')

    class Meta:
        model = ItemTag
        fields = ['item','tag',]

class AssortmentModelFilter(filters.FilterSet):
    item = filters.Filter(field_name='item_id', lookup_expr='exact')
    quantity = filters.CharFilter(lookup_expr='icontains')
    isInStock = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Assortment
        fields = ['item', 'quantity', 'isInStock']

class Order_ItemModelFilter(filters.FilterSet):
    order = filters.CharFilter(lookup_expr='icontains')
    item = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Order_Item
        fields = ['order','item',]