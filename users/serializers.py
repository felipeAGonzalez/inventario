from rest_framework import serializers
from .models import Users
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name','search','last_name_1','last_name_2','email','password','preferred_language','deleted','created_at','updated_at')
        read_only_fields = ('search','created_at','updated_at')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].write_only = True 
    
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()    
        return instance   