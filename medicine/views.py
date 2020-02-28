from django.shortcuts import render,get_object_or_404
from .models import medicine
def tablet(request):
    tablet = medicine.objects
    return render(request, 'medicine/tablet.html', {'tablet':tablet})
def detials(request,medicine_id):
    tablet = get_object_or_404(medicine, pk=medicine_id)
    return render(request, 'medicine/detials.html', {'tablet':tablet})