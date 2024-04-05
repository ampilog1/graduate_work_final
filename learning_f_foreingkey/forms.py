from django import forms


class text_to_send(forms.Form):
    text_to_send = forms.CharField(max_length=100)