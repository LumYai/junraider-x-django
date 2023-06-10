from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('', views.home, name='home'),
    path('subscription', views.ssubscription, name='subscription'),
    path('subscription/thankyou', views.subscription_thankyou, name='subscription_thankyou'),
]