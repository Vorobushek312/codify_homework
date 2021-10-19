from django import forms

class CalculatorForm(forms.Form):
    first_number = forms.FloatField()
    second_number = forms.FloatField()
    #operation = forms.CharField()
    CHOICES = (('+', 'Сложить'),('-', 'Вычесть'),('*', 'Умножить'),('/', 'Разделить'),('**', 'Возвести в степень'),)
    operation = forms.ChoiceField(choices=CHOICES)