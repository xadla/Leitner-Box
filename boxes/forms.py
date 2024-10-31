from django import forms


class AddWordForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "name_word", "placeholder": "Enter The Word..."},
        ),
    )

    example = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "explain_word", "placeholder": "Enter The Info..."}
        ),
        required=False,
    )

    definition = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "explain_word", "placeholder": "Enter The Definition..."}
        ),
        required=False,
    )

class AddBoxForm(forms.Form):

    capacity = forms.IntegerField(
        min_value=1,
        max_value=100,
        required=False
    )