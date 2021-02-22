from django.http.request import RawPostDataException
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'reg/reg.html',{'form':form})