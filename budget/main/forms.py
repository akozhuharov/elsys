from django import forms


class AddForm(forms.Form):
    amount = forms.FloatField()
    type = forms.ChoiceField(choices=(("IN", "IN"), ("OUT", "OUT")))
