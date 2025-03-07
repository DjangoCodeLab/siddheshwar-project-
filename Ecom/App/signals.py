from django.db.models.signals import pre_save 
from django.dispatch import receiver 
from .models import CartItem 

@receiver(pre_save,sender = CartItem)
def reduce_stock(sender,instance,**kwargs):
    if instance.pk is None:
        if instance.product.stock>=instance.quantity:
            instance.product.stock -=instance.quantity 
            instance.product.save()
        else:
            raise ValueError("not enough stock available!")
        
        