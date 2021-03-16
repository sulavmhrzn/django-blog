from django import forms


class SendEmailForm(forms.Form):
    your_name = forms.CharField(label='Your name')
    email = forms.EmailField(label='Recievers Email')
