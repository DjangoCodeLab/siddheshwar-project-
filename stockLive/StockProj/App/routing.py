from django.urls import re_path 
from App.consumers import StockConsumer

websocket_urlpattern = [
    re_path(r'ws/stocks/$',StockConsumer.as_asgi())
]