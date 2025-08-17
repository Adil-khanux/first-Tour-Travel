from django import forms

class meraform(forms.Form):
    num1=forms.CharField(label="Value1",required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
    # CATEGORY_CHOICES = [
    #     ('+', '+'),
    #     ('-', '-'),
    #     ('books', 'Books'),
    # ]
    # category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)

    num2=forms.CharField(label="Value2",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))


    