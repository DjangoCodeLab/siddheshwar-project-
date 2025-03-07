import requests
import os
import django
import decimal
from django.core.files.base import ContentFile
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecom.settings')
django.setup()
from django.db.models import *
from App.models import *
# Q1: Retrieve all products in the Product model with a price greater than ₹1000.
# product = Product.objects.filter(price__gte = 1000)
# print(product.values_list()[:10])

# for i in product:
#     print(i.title, i.price)

# # Q2: Retrieve all categories in the Category model that contain the word "Electronics" in their name.
# category = Category.objects.filter(category__icontains = "Gro")
# print(category)

# # Q3: Find all products that are out of stock (where stock = 0).
# stock_of_product = Product.objects.filter(stock = 0)
# for i in stock_of_product:
#     print(i.title,i.stock)


# # Q4: Get all products in the Product model that have a discount percentage greater than 20%.
# discount_percentage_val = Product.objects.filter(discount_percentage__gte = 10.0).values('title','discount_percentage')
# print(discount_percentage_val)


# # Q1: Retrieve the top 5 products in terms of rating.
# Top_Five_Product = Product.objects.all().order_by('-rating')[:5]
# # print(Top_Five_Product)
# for product in Top_Five_Product:
#     print(f"Prdouct Name:{product.title} \n Product Price:{product.price} \n Product Rating:{product.rating} \n")


# product_cat = Category.objects.annotate(count_product = Count('cat__title'))


# for product in product_cat:
#     print(product.category,product.count_product)

# Avaliablity_product = Product.objects.filter(availabilityStatus = "In Stock")

# for product in Avaliablity_product:
#     print(f"Product id:{product.id}||Product title:{product.title}||-||Product stock:{product.availabilityStatus}")


# # Q1: Find the total number of products in the Product model.
# sum_of_product = Product.objects.aggregate(total_count = Count('title'))

# print(sum_of_product)


# # Q2: Calculate the average price of all products in the database.
# avg_of_product = Product.objects.aggregate(avg_price = Avg('price'))

# print(avg_of_product)

# sum_of_discount = Product.objects.aggregate(total_discount = Sum('discount_percentage'))
# print(sum_of_discount)

# min_price_product = Product.objects.aggregate(max_price = Max('price'))
# print(min_price_product)
# print(min_price_product['max_price'])


# update_product = Product.objects.get(id = 197)

# update_product.stock = 100
# update_product.save()

# print(f"Product Title:{product.title} - stock:{product.stock}")

# increase_product_price = Product.objects.get(id = 320)
# increase_product_price.price = (increase_product_price.price + (increase_product_price.price * decimal.Decimal(0.1)))
# print(increase_product_price.price)

# out_of_stock_product = Product.objects.filter(availabilityStatus = "Out of Stock")

# for product in out_of_stock_product:
#     print(product.title,product.stock)


# count_of_each_product = Category.objects.annotate(product_count = Count('cat__title'))

# for category in count_of_each_product:
#     print(f'Category:{category} - Count Of each Catgory product:{category.product_count}')

# products_with_iamges = Product.objects.filter(product_images__isnull = False).distinct()

# print(products_with_iamges)

# category = Category.objects.all()
# print(category)
# product = Product.objects.all()

# prod_cate = product.filter(category__category = 'motorcycle')
# print(prod_cate)

# discount_product = product.filter(discount_percentage__gte = 10).values('title','discount_percentage')
# print(discount_product)

# unique_stock = Product.objects.distinct('availabilityStatus').values_list('availabilityStatus')
# print(unique_stock)

# stock = Product.objects.filter(availabilityStatus = "In Stock").values_list('title','price','availabilityStatus')
# print(stock)

# category_prod_count = Category.objects.annotate(total_count = Count('cat__title'))
# for i in category_prod_count:
#     print(i.category)
#     print(i.total_count)

# product = Product.objects.all().order_by('-price')[:5].values_list('title','price')
# print(product)

# product = Images.objects.filter(images__isnull = False).distinct().values_list('product__title','images')
# # print(product)

# product = Category.objects.annotate(Total_number_of_product_count = Count('cat__title'))
# print(product)

# product = Product.objects.filter(sku__startswith = "ABC")
# print(product)

# product = Product.objects.aggregate(total_value = Sum(F('price') * F('stock')))
# print(product)

# product = Product.objects.all().update(discount_percentage = F('discount_percentage') * 0)

# product = Product.objects.all().values_list('title','discount_percentage')
# print(product)

product = Product.objects.all()
product.delete()

