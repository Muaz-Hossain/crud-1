from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistation
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistation(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistation()
    else:
        fm = StudentRegistation()
    stud = User.objects.all()
        
    
    return render(request, 'enroll/addshow.html', {'form':fm, 'stu':stud})


#this function will update and edit

def update_data(request, id):
    if request.method == "POST":
        py = User.objects.get(pk=id)
        fm = StudentRegistation(request.POST, instance=py)
        if fm.is_valid():
            
            fm.save()
            
            
    else:
        py = User.objects.get(pk=id)
        fm = StudentRegistation(instance=py)
    return render(request, 'enroll/update.html', {'form': fm})



#this function will delete data

def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
    