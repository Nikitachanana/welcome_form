from . import forms
from django.shortcuts import render
from . import models
from . import forms

def Details(request):
    # if request.method == 'POST':


    details= models.UserDetails.objects.all()
    data= details[0]
    form = forms.DetailsForm(initial= {'name':data.name,'username':data.username,'phone': data.phone, 'skills': data.skills,
                                      'dob': data.dob, 'email': data.email, 'empStatus': data.empStatus })
    if request.method == "POST":
        form = forms.DetailsForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['name']
            b = form.cleaned_data['username']
            f = form.cleaned_data['phone']
            g = form.cleaned_data['dob']
            e = form.cleaned_data['email']
            c = form.cleaned_data['skills']
            d = form.cleaned_data['empStatus']
            details[0] = details(name=a, username=b, skills=c, empStatus=d, email=e, phone=f, dob=g)
            details.save()
    return render(request, "index.html", {'data': data ,'form': form })


# def Details(request):
#     if request.method == 'POST':
#         details= models.UserDetails.objects.all()
#         data = details[0]
#         form = forms.DetailsForm(initial= {'name':data.name,'username':data.username,'phone': data.phone, 'skills': data.skills,
#         #                               'dob': data.dob, 'email': data.email, 'empStatus': data.empStatus })
#         # if form.is_valid():
#         #     data=form.cleaned_data
#         #     data.save()
# return render(request, "index.html", {'data': data ,'form': form })




