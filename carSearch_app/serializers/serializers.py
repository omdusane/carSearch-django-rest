from rest_framework import serializers
from ..models import Carlist , Showroomlist, Review

class ReviewSerializer(serializers.ModelSerializer):
    apiuser = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Review
        exclude = ('car',)
        # fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many = True ,read_only = True )

    class Meta:         
        model = Carlist
        fields = "__all__"
    
    def get_discounted_price(self,obj):
        return obj.price - 5000
    
class ShowroomSerializer(serializers.ModelSerializer):
    showrooms = CarSerializer(many = True, read_only = True)
    class Meta:
        model = Showroomlist
        fields = "__all__"
    