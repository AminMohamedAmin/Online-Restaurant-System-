from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:slug>/', views.product, name='product'),
    path('reserve/', views.reserve, name='reserve'),
    path('reserves/', views.reservations, name='reserves'),
    path('reservesfound/', views.reservationsFound, name='reservesfound'),
    path('updatetable/<int:id>/', views.updatetable, name='updatetable'),
    path('saveupdatetable/<int:id>/', views.saveupdatetable, name='saveupdatetable'),
    path('deletetable/<int:id>/', views.deletetable, name='deletetable'),
    path('complaint/', views.complaints, name='complaint'),
    path('apply/', views.applying, name='apply'),
    path('inlog/', views.inlogpage, name='inlog'),
    path('saveinlog/', views.saveinlog, name='saveinlog'),
    path('saveinlog2/', views.saveinlog2, name='saveinlog2'),
    path('outlog/', views.outlog, name='outlog'),
]