from django import forms

class BulkUploadForm(forms.Form):
    input = forms.CharField(widget=forms.Textarea)

class PriceIncreaseForm(forms.Form):
    percentage = forms.IntegerField()
