 
from django.contrib import admin 
from django.urls import path
from sample import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sutcreate/',views.student_create ),


]
