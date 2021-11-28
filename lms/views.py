
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,logout

from django.contrib import messages

from lms.models import UserInput , Books , Customer

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginpage(request):
    if request.session.has_key('is_logged'):
        return redirect('homepage')
    return render(request,'loginpage.html')
def homepage(request):
    if request.session.has_key('is_logged'):
      
        return render(request,'homepage.html')
      
def signup(request):
    return render(request,'signup.html')   
def LoginBackend(request):
    if request.method =='POST':
        username = request.POST["username"]  
    return render(request,'homepage.html')     

def summary(request):
    Book = Books.objects.all()
    return render(request,'summary.html',{'Book':Book}) 

def addstudent(request):
 
    return render(request,'addstudent.html')

def addstudentsubmission(request):
        if request.method == "POST":

            
            name = request.POST["name"]
            
            age = request.POST["age"]
           
            #bookno = Books.objects.get(id=id)
            issuedate = request.POST["issuedate"]
            add = Customer(name = name,age=age,issuedate=issuedate)
            add.save()
            Student = Customer.objects.all()
            return render(request,'addstudent.html',{'Student':Student})
   

   



    


def display(request):
	st=Books.objects.all() # Collect all records from table 
	return render(request,'display.html',{'st':st})

def displaycust(request):
	ct=Customer.objects.all() # Collect all records from table 
	return render(request,'customer.html',{'ct':ct})   


def addbook(request):
    Book = Books.objects.all()
    return render(request,'addbook.html',{'Book':Book})


def AddBookSubmission(request):
   
        if request.method == "POST":
             
        
            bookno = request.POST["bookno"]
            name = request.POST["name"]
            author = request.POST["author"]
            issuedate = request.POST["issuedate"]
            
            add = Books(bookno=bookno,name=name,author=author,issuedate=issuedate)
            add.save()
            Book = Books.objects.all()
            return render(request,'homepage.html',{'Book':Book})





             
