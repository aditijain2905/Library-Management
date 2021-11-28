from django.contrib import admin
from django.urls import path , include
from lms import views


urlpatterns = [
    
     path('',views.index,name='index'),
     path('login/',views.login,name='login'),
      path('loginpage/',views.loginpage,name='loginpage'),
   path('signup/',views.signup,name='signup'),
    path('homepage/',views.homepage,name='homepage'),
    path('display/',views.display,name='display'),
    path('Customer/',views.displaycust,name='Customer'),
    
	path('books/display',views.display,name='display'),

    path('summary/',views.summary,name='summary'),

    path('addbook/',views.addbook,name='addbook'),
   
    path('LoginBackend/',views.LoginBackend,name='LoginBackend'),
    path('AddBookSubmission/',views.AddBookSubmission,name='AddBookSubmission'),

    
    path('addstudent/',views.addstudent,name='addstudent'),
    path('addstudentsubmission/',views.addstudentsubmission,name='addstudentsubmission')
    
]
