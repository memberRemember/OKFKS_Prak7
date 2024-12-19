from django.contrib import admin
from django.conf.urls import include
from django.urls import *
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import *
import LolzMarket.views as v

urlpatterns = [
    path('', v.index, name='index_page'),
    path('registration/', v.RegisterUser.as_view(), name='registration'),
    path('login/', v.AuthUser.as_view(), name='authuser'),
    path('login/token', ObtainAuthToken.as_view(), name='gettoken'),
    path('userlogout/', v.CustomLogoutView.as_view(), name='userlogout'),
    
    path('users/', v.UserListView.as_view(), name='user_list'),
    path('users/new', v.UserCreateView.as_view(), name='user_new'),
    path('users/update/<int:pk>', v.UserUpdateView.as_view(), name='user_update'),

    path('roles/', v.RoleListView.as_view(), name='role_list'),
    path('roles/new', v.RoleCreateView.as_view(), name='role_new'),
    path('roles/update/<int:pk>', v.RoleUpdateView.as_view(), name='role_update'),
    path('roles/delete/<int:pk>', v.RoleDeleteView.as_view(), name='role_delete'),
    
    path('statusorder/', v.StatusOrderListView.as_view(), name='statusorder_list'),
    path('statusorder/new', v.StatusOrderCreateView.as_view(), name='statusorder_new'),
    path('statusorder/update/<int:pk>', v.StatusOrderUpdateView.as_view(), name='statusorder_update'),
    path('statusorder/delete/<int:pk>', v.StatusOrderDeleteView.as_view(), name='statusorder_delete'),
    
    path('statuspayment/', v.StatusPaymentListView.as_view(), name='statuspayment_list'),
    path('statuspayment/new', v.StatusPaymentCreateView.as_view(), name='statuspayment_new'),
    path('statuspayment/update/<int:pk>', v.StatusPaymentUpdateView.as_view(), name='statuspayment_update'),
    path('statuspayment/delete/<int:pk>', v.StatusPaymentDeleteView.as_view(), name='statuspayment_delete'),
    
    path('paymentmethod/', v.PaymentMethodListView.as_view(), name='paymentmethod_list'),
    path('paymentmethod/new', v.PaymentMethodCreateView.as_view(), name='paymentmethod_new'),
    path('paymentmethod/update/<int:pk>', v.PaymentMethodUpdateView.as_view(), name='paymentmethod_update'),
    path('paymentmethod/delete/<int:pk>', v.PaymentMethodDeleteView.as_view(), name='paymentmethod_delete'),
    
    path('quality/', v.QualityListView.as_view(), name='quality_list'),
    path('quality/new', v.QualityCreateView.as_view(), name='quality_new'),
    path('quality/update/<int:pk>', v.QualityUpdateView.as_view(), name='quality_update'),
    path('quality/delete/<int:pk>', v.QualityDeleteView.as_view(), name='quality_delete'),
    
    path('rarity/', v.RarityListView.as_view(), name='rarity_list'),
    path('rarity/new', v.RarityCreateView.as_view(), name='rarity_new'),
    path('rarity/update/<int:pk>', v.RarityUpdateView.as_view(), name='rarity_update'),
    path('rarity/delete/<int:pk>', v.RarityDeleteView.as_view(), name='rarity_delete'),
    
    path('itemtype/', v.ItemTypeListView.as_view(), name='itemtype_list'),
    path('itemtype/new', v.ItemTypeCreateView.as_view(), name='itemtype_new'),
    path('itemtype/update/<int:pk>', v.ItemTypeUpdateView.as_view(), name='itemtype_update'),
    path('itemtype/delete/<int:pk>', v.ItemTypeDeleteView.as_view(), name='itemtype_delete'),
    
    path('category/', v.CategoryListView.as_view(), name='category_list'),
    path('category/new', v.CategoryCreateView.as_view(), name='category_new'),
    path('category/update/<int:pk>', v.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>', v.CategoryDeleteView.as_view(), name='category_delete'),

    path('tag/', v.TagListView.as_view(), name='tag_list'),
    path('tag/new', v.TagCreateView.as_view(), name='catgory_new'),
    path('tag/update/<int:pk>', v.TagUpdateView.as_view(), name='tag_update'),
    path('tag/delete/<int:pk>', v.TagDeleteView.as_view(), name='tag_delete'),

    path('item/', v.ItemListView.as_view(), name='item_list'),
    path('item/new', v.ItemCreateView.as_view(), name='item_new'),
    path('item/update/<int:pk>', v.ItemUpdateView.as_view(), name='item_update'),
    path('item/delete/<int:pk>', v.ItemDeleteView.as_view(), name='item_delete'),
        
    path('itemtag/', v.ItemTagListView.as_view(), name='itemtag_list'),
    path('itemtag/new', v.ItemTagCreateView.as_view(), name='itemtag_new'),
    path('itemtag/update/<int:pk>', v.ItemTagUpdateView.as_view(), name='itemtag_update'),
    path('itemtag/delete/<int:pk>', v.ItemTagDeleteView.as_view(), name='itemtag_delete'),
    
    path('orders/', v.OrderListView.as_view(), name='order_list'),
    path('orders/new', v.OrderCreateView.as_view(), name='order_new'),
    path('orders/update/<int:pk>', v.OrderUpdateView.as_view(), name='order_update'),
    path('orders/delete/<int:pk>', v.OrderDeleteView.as_view(), name='order_delete'),
    
    path('transactions/', v.TransactionsListView.as_view(), name='transaction_list'),
    path('transactions/new', v.TransactionsCreateView.as_view(), name='transaction_new'),
    path('transactions/update/<int:pk>', v.TransactionsUpdateView.as_view(), name='transaction_update'),
    path('transactions/delete/<int:pk>', v.TransactionsDeleteView.as_view(), name='transaction_delete'),
    
    path('assortment/', v.AssortmentListView.as_view(), name='assortment_list'),
    path('assortment/new', v.AssortmentCreateView.as_view(), name='assortment_new'),
    path('assortment/update/<int:pk>', v.AssortmentUpdateView.as_view(), name='assortment_update'),
    path('assortment/delete/<int:pk>', v.AssortmentDeleteView.as_view(), name='assortment_delete'),

    path('order_item/', v.Order_ItemListView.as_view(), name='order_item_list'),
    path('order_item/new', v.Order_ItemCreateView.as_view(), name='order_item_new'),
    path('order_item/update/<int:pk>', v.Order_ItemUpdateView.as_view(), name='order_item_update'),
    path('order_item/delete/<int:pk>', v.Order_ItemDeleteView.as_view(), name='order_item_delete'),
]

handler404 = v.page_not_found
