from django import forms


class DetailsForm(forms.Form):
    name = forms.CharField(label="Name",max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)
    dob = forms.CharField(label="DOB ", max_length=50, widget=forms.DateInput(attrs={'placeholder': 'DOB'}))
    username  = forms.CharField(label="Phone Number", max_length = 13, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),required=True)
    password = forms.CharField(label="Password", max_length=13, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),required=True)
    photo = forms.ImageField(required=True)
    email = forms.EmailField(label="Email Address", max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),required=True)
    phone = forms.CharField(label="Phone Number", max_length=13,
                            widget=forms.NumberInput(attrs={'placeholder': 'Phone Number'}),required=True)
    skills = forms.CharField(label="Skills",widget=forms.Textarea(attrs={'placeholder': 'Skills'}))
    joined = forms.CharField(label="Joined ", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Joined'}))

class CardForm(forms.Form):
    cardNumber = forms.CharField(label="Card Number",max_length=16, widget=forms.NumberInput(attrs={'placeholder': 'Card Number'}), required=True)
    expiryDate = forms.DateField(label="Expiry Date", max_length=50, widget=forms.DateInput(attrs={'placeholder': 'Expiry Date'}),required=True)
    cvv = forms.CharField(label="CVV", max_length=3, widget=forms.PasswordInput(attrs={'placeholder': 'CVV'}),required=True)









