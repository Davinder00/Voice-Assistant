"""
URL configuration for learning2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('about', include('home.urls')),
    # path('contact', include('home.urls')),
    # path('blogs', include('home.urls')),
    # path('genre', include('home.urls')),
    # path('newrelease', include('home.urls')),
    # path('topsellers', include('home.urls')),
    # path('morewriters', include('home.urls')),
    # path('morerecomendation', include('home.urls'))
    
    
    
    
    
]


admin.site.site_title = "Nirvana Admin"
admin.site.site_header = "Nirvana Admin"
admin.site.index_title = "Weclcome to Nirvana!"
