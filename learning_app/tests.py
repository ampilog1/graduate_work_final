from django.test import TestCase
from .forms import FindForm


class MyFormTest(TestCase):
    def test_form_valid_data_latin(self):
        form_data = {'vacancy_find': 'django'}
        form = FindForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_valid_data_cyrrilic(self):
        form_data = {'vacancy_find': 'стажер'}
        form = FindForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {'vacancy_find': '//**M**//'}
        form = FindForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('vacancy_find', form.errors)
        self.assertEqual(form.errors['vacancy_find'], ['Для ввода используютйте буквы пожалуста'])
