from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master', views.Master,name='master'),
    path('', views.index,name='index'),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

    #cartpath
    path('cart/add/<int:id>/', views.cart_add,name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear,name='item_clear'),
    path('cart/item_decrement/<int:id>/', views.item_decrement,name='item_decrement'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/cart_clear/', views.cart_clear,name='cart_clear'),
    path('cart/cart_detail/', views.cart_detail,name='cart_detail'),

    #Contact paths
    path('contact_us',views.ContactPage,name='contact_us'),

    #checkout
    path('checkout/',views.Checkout,name='checkout'),

    #order_page
    path('order/',views.Your_order,name='order'),

    #product_page
    path('product/',views.Product_page,name='product'),

    #product_details
    path('product/<int:id>',views.Product_Detail,name='product_detail'),

    #search
    path('search/',views.search,name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
