from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post,PostLog


@receiver(post_save,sender=Post)
def create_post_log(sender,instance,created,**kwargs):
    if created:
        PostLog.objects.create(post=instance)
        print("---------------------------")
        print("createed log for the saved post")
        print("---------------------------")
       

