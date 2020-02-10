from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import NameForm
from django.http import HttpResponseRedirect
def hello(request):
    return HttpResponse("Hello world")

def templateexample(request):
    return render(request,'inheit_template.html', {'title': "Django_MySQL_Boiler_Plate","body":"inherit template page"})
def appointment(request):
    return render(request,'appointmentrequest.html', {})
# def login1(request):
#     form = NameForm()
#     return render(request, 'login.html', {'form': form})
# from .models import Module


def ModuleManagement(request):
    pass


def ModuleAdd(request):
    if request.method == 'POST':
        r = request.POST
        username = r.get('username')
        password = r.get('pswd')
        # print(mname)
        # print(morder)
        if(username == "shusmoy" and password=="1234"):
            return redirect('appointment')
        # M = Module(name=mname, order=morder, category="config")
        # M.save()
        else:
            return redirect('ModuleAdd')
    else:
        context = {

        }
        return render(request, 'login.html', context)

def login(request):
   # if this is a POST request we need to process the form data
    print("hello")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("hello")
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/appointment/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login.html', {'form': form})