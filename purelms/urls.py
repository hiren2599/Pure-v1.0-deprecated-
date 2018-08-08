from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexView.as_view(),name='index'),
    path("backdoorlogin",views.backdoorloginView.as_view(),name='backdoorlogin'),
    path("<slug:coursecode>",views.courseHomeView.as_view(),name='courseHome')
]
