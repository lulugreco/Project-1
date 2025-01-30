from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
]

