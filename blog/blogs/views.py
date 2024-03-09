from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def trip(request):
    return render(request,'trip.html')
def cooking(request):
    return render(request,'cooking.html')
def dogs(request):
    return render(request,'dogs.html')
def kitchen(request):
    return render(request,'kitchen.html')
def height(request):
    return render(request,'height.html')