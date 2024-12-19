from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'nickname', 'email', 'is_active', 'role', 'role', 'balance', 'steamid', 'steam_profile_url', 'steam_avatar_url']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['rolename']

class StatusOrderForm(forms.ModelForm):
    class Meta:
        model = StatusOrder
        fields = ['statusOrderName']

class StatusPaymentForm(forms.ModelForm):
    class Meta:
        model = StatusPayment
        fields = ['statusPaymentName']
        
class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['paymentMethodName']
        
class QualityForm(forms.ModelForm):
    class Meta:
        model = Quality
        fields = ['qualityName']
              
class RarityForm(forms.ModelForm):
    class Meta:
        model = Rarity
        fields = ['rarityName'] 
        
class ItemTypeForm(forms.ModelForm):
    class Meta:
        model = ItemType
        fields = ['itemTypeName']
                
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['statusOrder','user','price']
                        
class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['order','paymentMethod','statusPayment']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')
                
class ItemTagForm(forms.ModelForm):
    class Meta:
        model = ItemTag
        fields = ('__all__')

class Order_ItemForm(forms.ModelForm):
    class Meta:
        model = Order_Item
        fields = ('__all__')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('__all__')
        
class AssortmentForm(forms.ModelForm):
    class Meta:
        model = Assortment
        fields = ('__all__')