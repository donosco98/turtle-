from django.contrib import admin
from django.urls import path,include,re_path
from . import views

app_name='quiz'

urlpatterns=[
     path('list/',views.question_list),
     path('list/<int:id>', views.question_details),
     path('list/create',views.add_question),




]
