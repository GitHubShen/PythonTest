from django.shortcuts import render
#from django.views.decorators import csrf

def CheckPassword(request):
    if request.POST and 'woaidaguanjia' == request.POST['Password'].lower():
        return render(request, 'Second.html')
