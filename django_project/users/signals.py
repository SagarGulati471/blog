from django.db.models.signals import post_save
from django.contrib.auth.models import User  
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)           #This create_profile func runs everytime when a user is created (#Jaise hi obj create hoga ye run hoga)
def create_profile(sender,instance,created,**kwargs):
    if created :
        Profile.objects.create(user=instance)



@receiver(post_save,sender=User)           #This save_profile func saves our profile when a user is created
def save_profile(sender,instance,**kwargs):
   instance.profile.save() 