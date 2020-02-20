from django import forms


class WelcomeForm(forms.Form):
    options=(
        ("Python", "Python"),
        ("Java", "Java"),
        ("PHP", "PHP"),
        ("iOS", "iOS"),
        ("Android", "Android"),
        (".Net", ".Net"),
        ("C/C++", "C/C++")
    )
    option=(
        ("male", "male"),
        ("female", "female")
    )
    name = forms.CharField(max_length=50)
    phone  = forms.CharField( max_length = 13, widget=forms.TextInput())
    email = forms.EmailField( max_length=50,
                             widget=forms.TextInput())
    dob = forms.CharField(max_length=13, widget=forms.DateInput())
    gender = forms.ChoiceField(widget=forms.RadioSelect(choices=option))
    college = forms.CharField( max_length=50, widget=forms.TextInput())
    degree = forms.CharField(max_length=50, widget=forms.TextInput())
    semester = forms.CharField( max_length=13,
                            widget=forms.TextInput())
    languages = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=options)
    interested = forms.CharField( max_length=50, widget=forms.TextInput())
    demo = forms.BooleanField()
    demoDate = forms.CharField( max_length=50, widget=forms.DateInput())