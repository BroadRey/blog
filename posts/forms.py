from django import forms


class PostCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=3, max_length=36)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()
