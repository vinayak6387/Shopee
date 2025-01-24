from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.
class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.is_vendor():
            return '/accounts/vendor/dashboard'
        elif self.request.user.is_buyer():
            return '/accounts/buyer/dashboard'
        return '/accounts/user/dashboard/' 
    
class UserRegistrataionView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
      return '/accounts/login/'
  
class VenderDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/vendor_dashboard.html'  
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_vendor():
            return redirect(no_permission)
        return super().dispatch(request, *args, **kwargs)
    

class BuyerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/buyer_dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_buyer():
            return redirect(no_permission)
        return super().dispatch(request, *args, **kwargs)
    
class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/user_dashboard.html'  
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_user():
            return redirect(no_permission)
        return super().dispatch(request, *args, **kwargs)    
    
def no_permission(request):
    return render(request, 'no_permission.html')      