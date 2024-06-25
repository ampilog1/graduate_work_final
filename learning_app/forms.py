from django import forms
from django.core.validators import RegexValidator


class FindForm(forms.Form):
    vacancy_find = forms.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                r'^[a-zA-Zа-яА-ЯёЁ \-_]*$',
                'Для ввода используйте только буквы, пробелы и тире, пожалуйста'
            )
        ]
    )
