from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='home'),
    #path('product_details.html', views.detailPage, name='detail'),
    path('product_summary.html', views.summaryPage, name='summary'),
    path('product_details.html/<int:pk>/', views.detailPage, name='detail'),
    path('special_offer.html', views.specialOfferPage, name='special'),
    path('delivery.html', views.deliveryPage, name='delivery'),
    path('delete/<int:pk>/', views.deletePage, name='delete'),
    path('increase/<int:pk>/', views.increasePage, name='increase'),
    path('reduce/<int:pk>/', views.reducePage, name='reduce'),
    path('products.html', views.productPage, name='products'),
    path('cate', views.show_genres, name='cate'),
    path('category/<int:pk>', views.categoryPage, name='category'),
    path('payment.html', views.paymentPage, name='payment')
]
