from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator



class RegisterSerializer(serializers.ModelSerializer):
    #!Register islemi icin ilk adim burasi. serializers olusturuyoruz. daha sonra views de tanimliyouru. views i de urls de /register/ olarak belirtiyoruz.
    #!Auth dersinden Copy-Past edildiler  
    email=serializers.EmailField(                                   #!email i zorunlu hale getiriyoruz. override ile
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]   #! gelen objelerin hepsini al. girilen emailde validator islemine sok. eger eslesen varsa. daha önce kullanilmamis bir email yazmasini söyle.
        )       
    password=serializers.CharField(
        write_only=True,                     #! request de al kullan. response da verme...
        required=True,
        style={"input_type" : "password"}    #!front end de. password typeinde input area olusturu. . . . gözükür yani.
        )
    password2=serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type" : "password"}    #!browsable api icin 
        )  

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'  
        ]

    def validate(self, data):                         #!raise a error if passwords dint't match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"message" : "Password1 and Possword2 didn't match."})
        return data
    
    def create(self, validated_data):       #!validate ettigim datadan.password2 cikar. cünkü modelimde öyle birsey yok. 
        validated_data.pop('password2')               #!db de yok o yüzden çıkar
        password=validated_data.pop('password')       
        user=User.objects.create(**validated_data)    #!passwordlari cikarinca obj create
        user.set_password(password)                   #! hash leme işlmi
        user.save()
        return user
    

#! Normal TokenSerializersin responsunu degistirmek istiyoruz. Sadece key dönmesin o key e ait users da gelsin.  
from dj_rest_auth.serializers import TokenSerializer

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name"  
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):            #!metayi inherit et..
        fields = (
            "key",
            "user"                               #! bu user icin UserTokenSerializer olusturduk in line 53
            ) 
        
#! CustomTokenSerializer base.py da tanimlamaliyiz