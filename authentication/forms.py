from django import forms
from . import models

class SkinUpload(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['skin']


class CloakUpload(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['cloak']
