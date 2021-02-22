from django.shortcuts import render
from .forms import UserProfile
from .models import UserForm
# Create your views here.
def home(request):
    return render(request,'first/home.html')
def datashow(request):

    data=UserForm.objects.order_by('firstname')

    return render(request,'first/datashow.html',{'data':data})

def form(request):
    form=UserProfile()
    if request.method =='POST':
        form=UserProfile(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanks(request)
    else:
        form=UserProfile()
    return render(request,'first/form.html',{'form':form})

def thanks(request):
    return render(request,'first/thanks.html')