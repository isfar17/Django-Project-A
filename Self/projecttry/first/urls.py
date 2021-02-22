from django.urls import path
from .import views

app_name='first'

urlpatterns = [
    path('',views.home,name='home'),
    path('datashow/',views.datashow,name='datashow'),
    path('form/',views.form,name='form'),
    path('thanks/',views.thanks,name='thanks'),


]