from django import forms


class AddWordForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "name_word", "placeholder": "Enter The Word..."},
        ),
    )

    explain = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "explain_word", "placeholder": "Enter The Info..."}
        ),
    )

class AddBoxForm(forms.Form):

    capacity = forms.IntegerField(
        min_value=1,
        max_value=100,
        required=False
    )