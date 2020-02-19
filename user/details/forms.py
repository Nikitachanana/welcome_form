from django import forms


class DetailsForm(forms.Form):
    name = forms.CharField(label="Name",max_length=50, widget=forms.TextInput(),required=True)
    dob = forms.CharField(label="DOB ", max_length=50, widget=forms.DateInput())
    username  = forms.CharField(label="Phone Number", max_length = 13, widget=forms.TextInput(),required=True)
    password = forms.CharField(label="Password", max_length=13, widget=forms.PasswordInput(),required=True)
    photo = forms.ImageField(required=True)
    email = forms.EmailField(label="Email Address", max_length=50,
                             widget=forms.TextInput(),required=True)
    phone = forms.CharField(label="Phone Number", max_length=13,
                            widget=forms.NumberInput(),required=True)
    skills = forms.CharField(label="Skills",widget=forms.TextInput())
    empStatus = forms.CharField(label="Employment Status", widget=forms.TextInput())
    joined = forms.CharField(label="Joined ", max_length=50, widget=forms.TextInput())

class CardForm(forms.Form):
    cardNumber = forms.CharField(label="Card Number",max_length=16, widget=forms.NumberInput(attrs={'placeholder': 'Card Number'}), required=True)
    month = forms.CharField(label="Month", max_length=2,
                             widget=forms.TextInput(attrs={'placeholder': 'Month'}),required=True)
    year = forms.CharField(label="Year", max_length=4,
                     widget=forms.TextInput(attrs={'placeholder': 'Year'}), required=True)
    cvv = forms.CharField(label="CVV", max_length=3, widget=forms.PasswordInput(attrs={'placeholder': 'CVV'}),required=True)









