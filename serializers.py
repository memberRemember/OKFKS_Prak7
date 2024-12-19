from rest_framework import serializers
from .models import *
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    # login = serializers.CharField(max_length=25)
    # password = serializers.CharField(max_length=255)
    # nickname = serializers.CharField(max_length=25)
    # email = serializers.EmailField(read_only=True)
    # date_created = serializers.DateTimeField(read_only=True) 
    # isActive = serializers.BooleanField(default=True)
    # role_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     #return User.objects.create(**validated_data)
    #     instance = User.objects.create(**validated_data)
    #     instance.create_date = datetime.datetime.now()
    #     return instance

    # def update(self, instance, validated_data):
    #     instance.login = validated_data.get("login", instance.login)
    #     instance.password = validated_data.get("password", instance.password)
    #     instance.nickname = validated_data.get("nickname", instance.nickname)
    #     instance.email = validated_data.get("email", instance.email)
    #     if 'date_created' in validated_data:
    #         instance.date_created = validated_data['date_created']
    #     instance.isActive = validated_data.get("isActive", instance.isActive)
    #     instance.role_id = validated_data.get("role_id", instance.role_id)
    #     instance.save()
    #     return instance

    class Meta:
        model = User
        fields = ('__all__')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')

class StatusPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPayment
        fields = ('__all__')

class StatusOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOrder
        fields = ('__all__')

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('__all__')

class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = ('__all__')

class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = ('__all__')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('__all__')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')

class ItemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTag
        fields = ('__all__')

class Order_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = ('__all__')
