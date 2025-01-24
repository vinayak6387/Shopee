from django.urls import path
from .views import CustomLoginView, UserRegistrataionView, VenderDashboardView, BuyerDashboardView, no_permission

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', UserRegistrataionView.as_view(), name='register'),
    path('vendor/dashboard/', VenderDashboardView.as_view(), name='vender_dashboard'),
    path('buyer/dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('user/dashboard/', UserRegistrataionView.as_view(), name='user_dashboard'),
    path('no_permission/', no_permission, name='no_permission')
    
]
