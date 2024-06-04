from rest_framework import serializers
from ..models import Carlist

def alphanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("Only Alphanumeric characters are allowed")

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only =  True)
    chassisnumber = serializers.CharField(validators = [alphanumeric])
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Carlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.chassisnumber = validated_data.get('chassisnumber', instance.chassisnumber)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    
    def validate_price(self, value):
        if value < 50000:
            raise serializers.ValidationError("Price must be greater than 50000")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise  serializers.ValidationError("Name and description can not be same.")
        return data