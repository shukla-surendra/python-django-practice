from django import forms

'''
Below link contain everything about django form

https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
'''

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    address = forms.CharField(max_length=100,  widget=forms.Textarea)