# from django.contrib import admin
# from django.urls import path, include
# from . import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('hello/', include('hello_world.urls'))
# ]

from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

