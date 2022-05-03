from django.contrib import admin
from django.urls import include, path, reverse
from django.shortcuts import redirect

urlpatterns = [
    # path('', views.index, name='index'),
    path(r'micontinfo/', include('micontinfo.urls', namespace='micontinfo')),
    path('', lambda x: redirect(reverse('micontinfo:index')), name='index'),
    
    path('admin/', admin.site.urls),

]
