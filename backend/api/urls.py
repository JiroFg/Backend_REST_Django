from django.urls import path
from . import views

urlpatterns = [
    path('user/get', views.getUsers),
    path('user/add', views.postUser),
    path('user/edit/<int:pk>', views.putUser),
    path('user/delete/<int:pk>', views.deleteUser),
    path('cr/get', views.getCrs),
    path('cr/add', views.postCr),
    path('cr/edit/<int:pk>', views.putCr),
    path('cr/delete/<int:pk>', views.deleteCr),
    path('iucr/get', views.getIUCrs),
    path('iucr/getByUser/<int:pk>', views.getIUCrsByUser),
    path('iucr/getByNum/<int:pk>', views.getIUCrsByNum),
    path('iucr/add', views.postIUCr),
    path('iucr/edit/<int:pk>', views.putIUCr),
    path('iucr/delete/<int:pk>', views.deleteIUCr),
]