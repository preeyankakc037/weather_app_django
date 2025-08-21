 # DAY 1: Building a weather application using Django 

 1. run the command ` django-admin startproject weatherproject `
 note use . at the end of the project like: `django-admin startproject weatherproject .`
to avoid double weatherproject folder 

2. We have to make another app so that we can perform all the operation  in it 
`django-admin startapp weatherapp `

3. Now run the server ` python manage.py runserver `



# Important files we  will be working on 

> Views.py 
views are python function that takes http request and return us HTTP response like: HTML documents and other 

> urls.py 
will create all the path of our application and how it will render 


# Process Documentation 

1. Creating urls.py in weatherapp
write this code in urls.py of weatherapp 

from django.urls import path 
from .import views

urlpatterns=[
    path('',views.home),
]


# Day 2 

1. Making templates and static folders 
2. Then we'll add API key in views.py 
3. Creating an venv file command ` python -m venv venv `

# Day 3 
Desigining HTML Template Properly 

# Day 4