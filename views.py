from django.shortcuts import *
from django.urls import reverse_lazy, reverse
from django.http import *
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.forms import *
from django.contrib.auth.views import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from rest_framework.authtoken.views import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from django.views.generic import *
from rest_framework import generics as genana
from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.pagination import *
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .paginations import *
from .filters import *
from .permissions import *
from .forms import *

def index(request):
    return render(request, './index.html')

def prikol(request):
    return render(request, './_prikol.html')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = './auth/registration.html'
    success_url = reverse_lazy('authuser')

class AuthUser(LoginView):
    form_class = AuthenticationForm
    template_name = './auth/login.html'
    success_url = 'index_page'
    def get_success_url(self):
        return reverse_lazy('index_page')
    
class CustomLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index_page')
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class ObtainAuthToken(APIView):
    renderer_classes = (renderers.BrowsableAPIRenderer,)


class UserListView(ListView):
    model = User
    template_name = './userlist.html'
    context_object_name = 'users'
    filterset_class = UserModelFilter
    ordering = ['login', 'password', 'nickname', 'email', 'date_created', 'is_active', 'role', 'balance', 'steamid', 'steam_profile_url', 'steam_avatar_url']

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = './user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = './user_form.html'
    success_url = reverse_lazy('user_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])



class RoleListView(ListView):
    model = Role
    template_name = './rolelist.html'
    context_object_name = 'roles'
    filterset_class = RoleModelFilter
    ordering = ['rolename']

class RoleCreateView(CreateView):
    model = Role
    form_class = RoleForm
    template_name = './role_form.html'
    success_url = reverse_lazy('role_list')

class RoleUpdateView(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = './role_form.html'
    success_url = reverse_lazy('role_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['role'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Role, pk=self.kwargs['pk'])

class RoleDeleteView(DeleteView):
    model = Role
    success_url = reverse_lazy('role_list')
    template_name = './role_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class StatusOrderListView(ListView):
    model = StatusOrder
    template_name = './statusorderlist.html'
    context_object_name = 'statusorders'
    filterset_class = StatusOrderModelFilter
    ordering = ['statusOrderName']

class StatusOrderCreateView(CreateView):
    model = StatusOrder
    form_class = StatusOrderForm
    template_name = './statusorder_form.html'
    success_url = reverse_lazy('statusorder_list')

class StatusOrderUpdateView(UpdateView):
    model = StatusOrder
    form_class = StatusOrderForm
    template_name = './statusorder_form.html'
    success_url = reverse_lazy('statusorder_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statusorder'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(StatusOrder, pk=self.kwargs['pk'])

class StatusOrderDeleteView(DeleteView):
    model = StatusOrder
    success_url = reverse_lazy('statusorder_list')
    template_name = './statusorder_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class StatusPaymentListView(ListView):
    model = StatusPayment
    template_name = './statuspaymentlist.html'
    context_object_name = 'statuspayments'
    filterset_class = StatusPaymentModelFilter
    ordering = ['statusPaymentName']

class StatusPaymentCreateView(CreateView):
    model = StatusPayment
    form_class = StatusPaymentForm
    template_name = './statuspayment_form.html'
    success_url = reverse_lazy('statuspayment_list')

class StatusPaymentUpdateView(UpdateView):
    model = StatusPayment
    form_class = StatusPaymentForm
    template_name = './statuspayment_form.html'
    success_url = reverse_lazy('statuspayment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuspayment'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(StatusPayment, pk=self.kwargs['pk'])

class StatusPaymentDeleteView(DeleteView):
    model = StatusPayment
    success_url = reverse_lazy('statuspayment_list')
    template_name = './statuspayment_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class PaymentMethodListView(ListView):
    model = PaymentMethod
    template_name = './paymentmethodlist.html'
    context_object_name = 'paymentmethods'
    filterset_class = PaymentMethodModelFilter
    ordering = ['paymentMethodName']

class PaymentMethodCreateView(CreateView):
    model = PaymentMethod
    form_class = PaymentMethodForm
    template_name = './paymentmethod_form.html'
    success_url = reverse_lazy('paymentmethod_list')

class PaymentMethodUpdateView(UpdateView):
    model = PaymentMethod
    form_class = PaymentMethodForm
    template_name = './paymentmethod_form.html'
    success_url = reverse_lazy('paymentmethod_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paymentmethod'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(PaymentMethod, pk=self.kwargs['pk'])

class PaymentMethodDeleteView(DeleteView):
    model = PaymentMethod
    success_url = reverse_lazy('paymentmethod_list')
    template_name = './paymentmethod_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class QualityListView(ListView):
    model = Quality
    template_name = './qualitylist.html'
    context_object_name = 'qualities'
    filterset_class = QualityModelFilter
    ordering = ['qualityName']

class QualityCreateView(CreateView):
    model = Quality
    form_class = QualityForm
    template_name = './quality_form.html'
    success_url = reverse_lazy('quality_list')

class QualityUpdateView(UpdateView):
    model = Quality
    form_class = QualityForm
    template_name = './quality_form.html'
    success_url = reverse_lazy('quality_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qualityName'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Quality, pk=self.kwargs['pk'])

class QualityDeleteView(DeleteView):
    model = Quality
    success_url = reverse_lazy('quality_list')
    template_name = './quality_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class RarityListView(ListView):
    model = Rarity
    template_name = './raritylist.html'
    context_object_name = 'rarities'
    filterset_class = RarityModelFilter
    ordering = ['rarityName']

class RarityCreateView(CreateView):
    model = Rarity
    form_class = RarityForm
    template_name = './rarity_form.html'
    success_url = reverse_lazy('rarity_list')

class RarityUpdateView(UpdateView):
    model = Rarity
    form_class = RarityForm
    template_name = './rarity_form.html'
    success_url = reverse_lazy('rarity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rarityName'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Rarity, pk=self.kwargs['pk'])

class RarityDeleteView(DeleteView):
    model = Rarity
    success_url = reverse_lazy('rarity_list')
    template_name = './rarity_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)
    


class ItemTypeListView(ListView):
    model = ItemType
    template_name = './itemTypelist.html'
    context_object_name = 'itemtypes'
    filterset_class = ItemTypeModelFilter
    ordering = ['itemTypeName']

class ItemTypeCreateView(CreateView):
    model = ItemType
    form_class = ItemTypeForm
    template_name = './itemType_form.html'
    success_url = reverse_lazy('itemType_list')

class ItemTypeUpdateView(UpdateView):
    model = ItemType
    form_class = ItemTypeForm
    template_name = './itemType_form.html'
    success_url = reverse_lazy('itemType_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itemTypeName'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(ItemType, pk=self.kwargs['pk'])

class ItemTypeDeleteView(DeleteView):
    model = ItemType
    success_url = reverse_lazy('itemType_list')
    template_name = './itemType_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)
    

class CategoryListView(ListView):
    model = Category
    template_name = './categorylist.html'
    context_object_name = 'categories'
    filterset_class = CategoryModelFilter
    ordering = ['categoryName', 'localizedName']

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = './category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = './category_form.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryName'] = self.object
        context['localizedName'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs['pk'])

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    template_name = './category_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class TagListView(ListView):
    model = Tag
    template_name = './taglist.html'
    context_object_name = 'tags'
    filterset_class = TagModelFilter
    ordering = ['tagName', 'category', 'localizedName']

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = './tag_form.html'
    success_url = reverse_lazy('tag_list')

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = './tag_form.html'
    success_url = reverse_lazy('tag_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagName'] = self.object
        context['localizedName'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Tag, pk=self.kwargs['pk'])

class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    template_name = './tag_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)
    

class OrderListView(ListView):
    model = Order
    template_name = './orderlist.html'
    context_object_name = 'orders'
    filterset_class = OrderModelFilter
    ordering = ['statusOrder', 'user', 'price']

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = './order_form.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = './order_form.html'
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statusOrder'] = self.object
        context['user'] = self.object
        context['price'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Order, pk=self.kwargs['pk'])

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders_list')
    template_name = './order_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)



class TransactionsListView(ListView):
    model = Transactions
    template_name = './transactionslist.html'
    context_object_name = 'transactions'
    filterset_class = TransactionsModelFilter
    ordering = ['order', 'paymentMethod', 'statusPayment']

class TransactionsCreateView(CreateView):
    model = Transactions
    form_class = TransactionsForm
    template_name = './transactions_form.html'
    success_url = reverse_lazy('transaction_list')

class TransactionsUpdateView(UpdateView):
    model = Transactions
    form_class = TransactionsForm
    template_name = './transactions_form.html'
    success_url = reverse_lazy('transaction_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.object
        context['paymentMethod'] = self.object
        context['statusPayment'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Transactions, pk=self.kwargs['pk'])

class TransactionsDeleteView(DeleteView):
    model = Transactions
    success_url = reverse_lazy('transaction_list')
    template_name = './transactions_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)



class ItemListView(ListView):
    model = Item
    template_name = './itemlist.html'
    context_object_name = 'items'
    filterset_class = ItemModelFilter
    ordering = ['assetid','name','name_color','name_on_market','description','quality','rarity','isStattrak','stattrak_stat','isTradable','isMarketable','type']

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = './item_form.html'
    success_url = reverse_lazy('item_list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = './item_form.html'
    success_url = reverse_lazy('itmem_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assetid'] = self.object
        context['name'] = self.object
        context['name_color'] = self.object
        context['name_on_market'] = self.object
        context['description'] = self.object
        context['quality'] = self.object
        context['rarity'] = self.object
        context['isStatTrak'] = self.object
        context['stattrak_stat'] = self.object
        context['isTradable'] = self.object
        context['isMarketable'] = self.object
        context['type'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Item, pk=self.kwargs['pk'])

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('item_list')
    template_name = './item_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class ItemTagListView(ListView):
    model = ItemTag
    template_name = './itemtaglist.html'
    context_object_name = 'itemtags'
    filterset_class = ItemTagModelFilter
    ordering = ['item', 'tag']

class ItemTagCreateView(CreateView):
    model = ItemTag
    form_class = ItemTagForm
    template_name = './itemtag_form.html'
    success_url = reverse_lazy('itemtag_list')

class ItemTagUpdateView(UpdateView):
    model = ItemTag
    form_class = ItemTagForm
    template_name = './itemtag_form.html'
    success_url = reverse_lazy('itemtag_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = self.object
        context['tag'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(ItemTag, pk=self.kwargs['pk'])

class ItemTagDeleteView(DeleteView):
    model = ItemTag
    success_url = reverse_lazy('itemtag_list')
    template_name = './itemtag_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class ItemTypeListView(ListView):
    model = ItemType
    template_name = './itemtypelist.html'
    context_object_name = 'itemtypes'
    filterset_class = ItemTypeModelFilter
    ordering = ['itemTypeName']

class ItemTypeCreateView(CreateView):
    model = ItemType
    form_class = ItemTypeForm
    template_name = './itemtype_form.html'
    success_url = reverse_lazy('itemtype_list')

class ItemTypeUpdateView(UpdateView):
    model = ItemType
    form_class = ItemTypeForm
    template_name = './itemtype_form.html'
    success_url = reverse_lazy('itemtype_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ItemType'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(ItemType, pk=self.kwargs['pk'])

class ItemTypeDeleteView(DeleteView):
    model = ItemType
    success_url = reverse_lazy('itemtype_list')
    template_name = './itemtype_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)



class AssortmentListView(ListView):
    model = Assortment
    template_name = './assortmentlist.html'
    context_object_name = 'assortments'
    filterset_class = AssortmentModelFilter
    ordering = ['item', 'quantity', 'isInStock']

class AssortmentCreateView(CreateView):
    model = Assortment
    form_class = AssortmentForm
    template_name = './assortment_form.html'
    success_url = reverse_lazy('assortment_list')

class AssortmentUpdateView(UpdateView):
    model = Assortment
    form_class = AssortmentForm
    template_name = './assortment_form.html'
    success_url = reverse_lazy('assortment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = self.object
        context['quantity'] = self.object
        context['isInStock'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Assortment, pk=self.kwargs['pk'])

class AssortmentDeleteView(DeleteView):
    model = Assortment
    success_url = reverse_lazy('assortment_list')
    template_name = './assortment_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)


class Order_ItemListView(ListView):
    model = Order_Item
    template_name = './order_itemlist.html'
    context_object_name = 'order_items'
    filterset_class = Order_ItemModelFilter
    ordering = ['order', 'product']

class Order_ItemCreateView(CreateView):
    model = Order_Item
    form_class = Order_ItemForm
    template_name = './order_item_form.html'
    success_url = reverse_lazy('order_item_list')

class Order_ItemUpdateView(UpdateView):
    model = Order_Item
    form_class = Order_ItemForm
    template_name = './order_item_form.html'
    success_url = reverse_lazy('order_item_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.object
        context['product'] = self.object
        return context

    def get_object(self):
        return get_object_or_404(Order_Item, pk=self.kwargs['pk'])

class Order_ItemDeleteView(DeleteView):
    model = Order_Item
    success_url = reverse_lazy('order_item_list')
    template_name = './order_item_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.exist = False
        self.object.save()
        return super().delete(request, *args, **kwargs)









def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена. 404</h1>")

""" 
########    API Views    ########
"""

"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperOrStaff]
    pagination_class = UserViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        if self.request.query_params.get('login') and self.request.query_params.get('password'):
            queryset = queryset.filter(
                login=self.request.query_params['login'],
                password=self.request.query_params['password']
            )
        return queryset
    
    

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = RoleViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoleModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class StatusPaymentViewSet(viewsets.ModelViewSet):
    queryset = StatusPayment.objects.all()
    serializer_class = StatusPaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = StatusPaymentViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = StatusPaymentModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class StatusOrderViewSet(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = StatusOrderViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = StatusOrderModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = PaymentMethodViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentMethodModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class QualityViewSet(viewsets.ModelViewSet):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = QualityViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = QualityModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = CategoryViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff, IsOwnerOrReadOnly]
    pagination_class = CommentsViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentsModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = OrderViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = TransactionsViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionsModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class ProductAccSteamViewSet(viewsets.ModelViewSet):
    queryset = ProductAccSteam.objects.all()
    serializer_class = ProductAccSteamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = ProductAccSteamViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductAccSteamModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset
    
    
    

@receiver(post_save, sender=ProductAccSteam_Games)
def update_vac_status_on_acc(sender, instance, created, **kwargs):
    if created or not instance.productAccSteam.isVAC == instance.isVAC:
        steam_account = instance.productAccSteam
        
        has_vac_ban = ProductAccSteam_Games.objects.filter(
            productAccSteam=steam_account, isVAC=True
        ).exists()
        
        if has_vac_ban:
            steam_account.isVAC = True
        else:
            steam_account.isVAC = False
        
        steam_account.save(update_fields=['isVAC'])

class AccSteamGamesViewSet(viewsets.ModelViewSet):
    queryset = AccSteamGames.objects.all()
    serializer_class = AccSteamGamesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = AccSteamGamesViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AccSteamGamesModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class ProductAccSteam_GamesViewSet(viewsets.ModelViewSet):
    queryset = ProductAccSteam_Games.objects.all()
    serializer_class = ProductAccSteam_GamesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = ProductAccSteam_GamesViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductAccSteam_GamesModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

class Order_ProductViewSet(viewsets.ModelViewSet):
    queryset = Order_Product.objects.all()
    serializer_class = Order_ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperOrStaff]
    pagination_class = Order_ProductViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = Order_ProductModelFilter
    def get_queryset(self):
        queryset = super().get_queryset()

        ordering = self.request.query_params.get('ordering', 'id')
        if ordering.startswith('-'):
            field = ordering[1:]
            queryset = queryset.order_by(f'-{field}')
        else:
            field = ordering
            queryset = queryset.order_by(f'{field}')

        return queryset

"""
