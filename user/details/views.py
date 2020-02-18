from . import forms
from django.shortcuts import render

def Details():
    if request.method == 'POST':
        form = forms.DetailsForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['name']
            b = form.cleaned_data['phone']
            c = form.cleaned_data['email']
            d = form.cleaned_data['password']
            e = form.cleaned_data['password2']
            details = Register(name=a, phone=b, email=c, password=d, confirm=e)
            details.save()
        else:
            form = forms.DetailsForm(request.POST)
    return render(request,'index.html',{'form': form )

