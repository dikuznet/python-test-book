from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View

# Create your views here.
class IndexView(View):
    # permission_required = 'auth.can_add_permissions'
    # PermissionRequiredMixin
    def get(self, request, arg=''):
        
        return render(
            request,
            'index.html',
        )
