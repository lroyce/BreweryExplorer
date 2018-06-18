from django.shortcuts import render

def signup(request):
    return render(request,'signup.html',{'title':'Signup'})

def login(request):
    pass

def logout(request):
    pass
