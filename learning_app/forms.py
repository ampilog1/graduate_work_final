from django import forms


class FindForm(forms.Form):
    vacancy_find = forms.CharField(max_length=100)
