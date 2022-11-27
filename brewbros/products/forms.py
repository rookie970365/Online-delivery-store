from django import forms
from products.models import ProductKind


class FilterByKindForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=ProductKind.objects.all(), label="",
                                    empty_label="--------------------")
