from django import forms


class CreateNewNote(forms.Form):
    note = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
