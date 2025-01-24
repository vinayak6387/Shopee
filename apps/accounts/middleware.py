from django.shortcuts import redirect

class RoleBaseRedirectMiddleware:
    def __init__(self, get_responce):
        self.get_responce = get_responce
        
    
    def __call__(self, request):
        if request.path.startswitch('/vendor') and not request.user.is_vendor():
            return redirect('no_permission')
        elif request.path.startswitch('/buyer') and not request.user.is_buyer():
            return redirect('no_permission')   
        return self.get_responce