from django.shortcuts import render, redirect
from client.forms import ClientForm
from client.models import Client




def emp(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ClientForm()
    return render(request,'client/index.html',{'form':form})
def show(request):
    emp = Client.objects.all()
    return render(request,'client/show.html',{'emp':emp})
