from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import  Token

#!decorator
@receiver(post_save, sender=User)               #!post_save save isleminden sonra yap. User da save islemi olduktan sonra.
def create_token(sender, instance, created=False, **kwargs): #!save isleminden sonra create 
    if created:
        Token.objects.create(user=instance)

#! User modelinde save islemi gerceklestikten sonra Token olussun istiyoruz. 


#!burayi olusturduktan sonra apps.py git. yazdigin signali import et. 