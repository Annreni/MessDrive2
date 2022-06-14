from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('test.html', views.test, name = 'test' ),
    path('index.html', views.index, name = 'index' ), 
    path('inmate.html', views.inmate, name = 'inmate')
]