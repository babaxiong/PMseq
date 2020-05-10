# coding:utf-8

from django.urls import path, include, re_path

from userAPP import views

urlpatterns ={
    path('', views.PMseq),
    path('find/', views.find , name='find'),
    path('findresult/', views.findresult),
    path('download/', views.download),
}
