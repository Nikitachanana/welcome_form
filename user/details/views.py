from django.shortcuts import render
from . import models
from . import forms


def details(request):
    # if request.method == 'POST':
    details = models.UserDetails.objects.all()
    data = details[0]
    print("Outside Post Method")
    if request.method == 'POST':
        form = forms.DetailsForm(request.POST)
        if form.is_valid():
            edit = form.cleaned_data
            print("Inside post method")
            print(edit['name'])
            data.name = edit['name']
            data.save()
    else:
        form = forms.DetailsForm(
            initial={'name': data.name, 'username': data.username, 'phone': data.phone, 'skills': data.skills,
                     'dob': data.dob, 'email': data.email, 'empStatus': data.empStatus})
    return render(request, "welcome.html", {'data': data,'form': form})


# def Details(request):
#     if request.method == 'POST':
#         details= models.UserDetails.objects.all()
#         data = details[0]
#         form = forms.DetailsForm(initial= {'name':data.name,'username':data.username,'phone': data.phone, 'skills': data.skills,
#         #                               'dob': data.dob, 'email': data.email, 'empStatus': data.empStatus })
#         # if form.is_valid():
#         #     data=form.cleaned_data
#         #     data.save()
# return render(request, "welcome.html", {'data': data ,'form': form })




