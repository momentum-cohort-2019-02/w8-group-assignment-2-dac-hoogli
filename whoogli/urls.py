"""whoogli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from core import views

#Add URL maps to redirect the base URL to our application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<slug:slug>/', views.question_detail, name='question_detail'),
    path('', RedirectView.as_view(url='/core/', permanent=True)),
    path('accounts/profile/', RedirectView.as_view(url='/questions/', permanent=True)),
    re_path(r'^accounts/', include('registration.backends.default.urls')),
    path('users/<str:username>/', views.profile, name='profile_page'),
]

# Use static() to add url mapping to serve static files during development (only)


# urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
