from rest_framework import serializers
from.models import Student


  
class  Studentserializer(serializers.Serializer):
    fast_name=serializers.CharField(max_length=100)
    last_Name=serializers.CharField(max_length=100)
    roll_No= serializers.IntegerField()
    ctye=serializers.CharField(max_length=100)


def create(self,validata_data):
    return Student.objects.create(** validata_data)    