from django import forms
from cart.models import Cart,URL

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = [
            'url',
        ]

