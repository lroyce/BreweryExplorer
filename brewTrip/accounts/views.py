from django.shortcuts import render

def signup(request):
    return render(request,'signup.html',{'title':'Signup'})

def login(request):
    return render(request, 'login.html',{'title':'Please Login'})

def logout(request):
    pass
