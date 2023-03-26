from rest_framework import viewsets, serializers
from django.contrib.auth.models import User

#Define password min_length
MIN_LENGTH = 8


#Overwrite default write pasword
class Userserializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages ={
            "min_length" : f"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    password2 = serializers.CharField(          #since password is usually entered twice
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages ={
            "min_length" : f"Password must be longer than {MIN_LENGTH} characters."
        }
    )
    
#Model for model serializer
    class Meta:
        model = User
        fields = "__all__"

#Make sure pass & pass2 are matching    
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data
    
#Overwrite serializers create method to save only one password after they match
    def create(self, validated_data):
        #note : creating user object to parse in data from class Meta Fields
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],   
        )
        
        #set userpass
        user.set_password(validated_data["password"])
        user.save()
        return user

#create viewsets 
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = Userserializer       
        