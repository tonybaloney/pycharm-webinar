from django import forms

class BulkUploadForm(forms.Form):
    data = forms.CharField(widget=forms.Textarea)

class PriceIncreaseForm(forms.Form):
    percentage = forms.IntegerField()
