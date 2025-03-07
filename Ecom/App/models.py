from django.db import models
from App.choices import *
import os
from django.conf import settings
from django.utils.text import slugify
User = settings.AUTH_USER_MODEL
# Create your models here.


def product_image_upload_path(instance, filename):
    safe_categroy_name = instance.product.category.category.replace(' ','-')
    safe_product_name = instance.product.title.replace(' ', '%20')
    return os.path.join('images',safe_categroy_name, safe_product_name, filename)


class Category(models.Model):
    category = models.CharField(max_length = 100,unique = True)
    category_slug = models.SlugField(unique=True,blank = True)   


    def __str__(self):
        return self.category
    
    class Meta:
        db_table = 'Category'

    
    def save(self,*args, **kwargs):
        if not self.category_slug:
            original_slug = slugify(self.category)
            self.category_slug = original_slug 
            counter = 1
            while Category.objects.filter(category_slug = self.category_slug).exists():
                self.category_slug = f"{original_slug}-{counter}"
                counter += 1
            super().save(*args,**kwargs)




class Product(models.Model):
    category = models.ForeignKey(Category, related_name='cat',on_delete=models.CASCADE,null=True, blank = True)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    discount_percentage = models.FloatField(max_length=5)
    rating  = models.IntegerField(default=0)
    stock = models.IntegerField()
    availabilityStatus = models.CharField(max_length = 100,choices=AVAILABLITY_STATUS)
    sku = models.CharField(max_length=20)
    product_slug = models.SlugField(default="",null=False)


    class Meta:
        db_table = 'Products'  # Removed duplicate Meta class

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.product_slug:  # Generate slug only if it's not already set
            original_slug = slugify(self.title)
            self.product_slug = original_slug
            counter = 1
            while Product.objects.filter(product_slug=self.product_slug).exists():
                self.product_slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)


    

class Dimensions(models.Model):
    product = models.ForeignKey(Product,related_name = "product_diamension",on_delete=models.CASCADE,null=True, blank = True)
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()

    def __str__(self):
        return f'{self.product.title} - {self.width} X {self.height} X {self.depth}'
    
    class Meta:
        db_table = 'Diamensions'




class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name = "product_images",null=True, blank = True)
    images = models.ImageField(upload_to=product_image_upload_path)

    

    class Meta:
        db_table = 'Images'


class Thumbnail(models.Model):
    product = models.ForeignKey(Product,related_name = "product_thumbnail",on_delete=models.CASCADE,null=True, blank = True)
    thumbnail = models.ImageField(upload_to=product_image_upload_path)


    def __str__(self):
        return f"{self.thumbnail} - Image"
    class Meta:
        db_table = 'Thumbnail'

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return f'{self.quantity} X {self.product.title}'
    
    class Meta:
        db_table = 'CartItem'


