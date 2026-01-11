"""
URL configuration for sticky_notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# Adding urls from tasks and todo_list apps

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# Define the URL patterns for the sticky_notes project
urlpatterns = [
    # Redirect root URL to tasks app home
    path('', RedirectView.as_view(url='/tasks/', permanent=False)),

    # Include admin site URLs
    path('admin/', admin.site.urls),

    # Include URLs from the tasks app
    path('tasks/', include('tasks.urls')),
    # Include URLs from the todo_list app
    path('todo/', include('todo_list.urls'))
]
