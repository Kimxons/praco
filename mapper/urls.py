from django.urls import path

from . import views

urlpatterns = [
path('',views.lecturer_list, name='index'),
#path('<int:lecturer_id>/', views.detail, name= 'detail'),
]