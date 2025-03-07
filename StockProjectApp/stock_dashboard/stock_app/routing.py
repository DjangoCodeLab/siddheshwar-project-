from django.urls import re_path
from stock_app.consumers import StockConsumer

websocket_urlpatterns = [
    re_path(r'ws/stocks/$',StockConsumer.as_asgi()),
]