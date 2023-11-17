from django import forms

class UplodeItems(forms.Form):
    SIZELIST = (
        ("select", "select"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
        ("none", "none"),
    )

    imgfile = forms.ImageField(required=True)
    title = forms.CharField( max_length=30, required=True)
    price = forms.IntegerField(required=True)
    Size = forms.ChoiceField(choices=SIZELIST, required=True)

