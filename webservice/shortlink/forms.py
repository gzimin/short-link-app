from django import forms
from .models import Link

forms.fields.Field.default_error_messages = {'required': (''),}


class ShortLinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ('source_url',)

class SourceLinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ('short_url',)
