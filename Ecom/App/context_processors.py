from App.models import *
from django.db.models import Count,Prefetch
def cart_count(request):
    if request.user.is_authenticated:
        total_items = CartItem.objects.filter(user= request.user).count()  
        print(total_items)
    else:
        total_items = 0
    
    return {"cart_total_items":total_items}


def category(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return context 

def theme_processor(request):
    theme = request.session.get('theme','light')
    return {'theme':theme}


def discount_product(request):
    categories = Category.objects.prefetch_related(
        Prefetch(
            'cat',  
            queryset=Product.objects.filter(discount_percentage__gt=10) 
        )
    ).filter(cat__discount_percentage__gt=10).distinct()  # Filter categories having discounted products

    # Extracting all products from these categories


    return {'categories': categories}
