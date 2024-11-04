from django import forms


class AddWordForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "name_word", "placeholder": "Enter The Name..."},
        ),
    )

    example = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "explain_word", "placeholder": "Enter The Examples..."}
        ),
        required=False,
    )

    definition = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "explain_word", "placeholder": "Enter The Definition..."}
        ),
        required=False,
    )