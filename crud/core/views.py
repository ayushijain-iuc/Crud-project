from django.shortcuts import render,redirect
from . forms import employeeform
from . models import Employee

def home(request):
    form=employeeform()
    if request.method=="POST":
        form=employeeform(request.POST)
        form.save()
        form=employeeform()
    data=Employee.objects.all()
    
    
    context={
        'form':form,
        'data':data,
    }
    return render(request,'index.html',context)


def delete(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect("/")
    
# Create your views here.
def update(request,id):
    if request.method=="POST":
        data=Employee.objects.get(pk=id)
        form=employeeform(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        data=Employee.objects.get(pk=id)
        form=employeeform(instance=data)
    context={"form":form,}
    return render(request,'update.html',context)