import requests
import os
import django
from django.core.files.base import ContentFile
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecom.settings')
django.setup()

from App.models import *
url = 'https://dummyjson.com/products?limit=1000'

response = requests.get(url)
data = response.json()
def add_category():
    categories= set()
    for i in data['products']:
        print(i['category'])
        categories.add(i['category'])

    
    for category in categories:
        cat = Category.objects.create(
            category = category
        )
        cat.save()
    return "Category Saved!"



def add_product():
    try:        
        products = []
        for product in data['products']:
            categroy_id = Category.objects.get(category = product['category'])
            prod = Product.objects.create(
                category = categroy_id,
                title = product['title'],
                description = product['description'],
                price = product['price'],
                discount_percentage = product['discountPercentage'],
                rating = product['rating'],
                stock = product['stock'],
                availabilityStatus = product['availabilityStatus'],
                sku = product['sku'],

            )
            prod.save()
        return "Products Saved"
    
    except Exception as e:
        print(e)

import random

def add_diamensions():
    for i in data['products']:
        product_id = Product.objects.filter(title = i['title']).first()
        width = i.get('dimensions', {}).get('width', random.uniform(1.0, 100.0))
        height = i.get('dimensions', {}).get('height', random.uniform(1.0, 100.0))
        depth = i.get('dimensions', {}).get('depth', random.uniform(1.0, 100.0))

        
        diamensions = Dimensions.objects.create(
            product = product_id,
            width = width,
            height = height,
            depth = depth,
        )
        diamensions.save()  
    return "Done"

# def download_image(image_url,save_dictionary,image_name):
#     if not os.path.exists(save_dictionary):
#         os.makedirs(save_dictionary)

#     image_path = os.path.join(save_dictionary,image_name)
#     response = requests.get(image_url,stream = True)
#     if response.status_code == 200:
#         with open(image_name,'wb') as file:
#             for chunk in response.iter_content(1024):
#                 file.write(chunk)
#     return image_url




def Save_images():
    for i in data['products']:
        products_id = Product.objects.filter(title = i['title']).first()
        # print(products_id)
        image_url = i.get('images')
        if len(image_url)<2:
            # response = requests.get(image_url)
            # print(image_url[0].split('/')[-1])
            img = Images.objects.create(
                        product=products_id,
                        images=ContentFile(response.content, name=image_url[0].split('/')[-1])
                    )
            img.save()
            
            
        else:
            for images in image_url:
                img = Images.objects.create(
                            product=products_id,
                            images=ContentFile(response.content, name=images.split('/')[-1])
                        )
                img.save()
                



def add_thumbnail():
    for i in data['products']:
        products_id = Product.objects.filter(title = i['title']).first()
        # print(products_id)
        thumb_url = i.get('thumbnail')
        thumbnail = thumb_url.split('/')[-1]
        img = Thumbnail.objects.create(
                        product=products_id,
                        thumbnail=ContentFile(response.content, name=thumbnail)
                    )
        img.save()
        
                
# add_category()
# add_product()
# add_diamensions()
Save_images()
# add_thumbnail()

# images = Images.objects.all()
# for i in images:
#     print(i.product)
#     print(i.images)


# def delete_product():
#     product = Category.objects.all()
#     product.delete()


# delete_product()