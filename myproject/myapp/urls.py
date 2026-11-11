from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),

    path('home/',views.Homepage, name="home"),
    path('about/',views.Aboutpage, name="about"),
    path('service/',views.Servicepage,name='service'),
    path('contact/',views.Contactpage,name='contact'),
    path('student/',views.Studentpage,name='student'),
    path('students/', views.Studentlist, name='students'),
    path('students/<int:pk>/edit/', views.Studentedit, name='student_edit'),
    path('students/<int:pk>/delete/', views.Studentdelete, name='student_delete'),
]

