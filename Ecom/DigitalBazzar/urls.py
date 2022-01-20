from django.urls import path
# from .views import Processing,Dash_board
from DigitalBazzar import views

urlpatterns = [
    path("",views.Product_View, name="products"),
    path('dashboard/',views.Dash_board,name='dash'),
    path('mycart/',views.Carts,name='mycart'),
    path('updatecart/',views.update_cart,name='updatecart'),
    path('shipping/',views.Shipping,name='shipping'),
    path('processing-orders/',views.Processing,name='processing'),
]
