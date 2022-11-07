from django.core.mail import send_mail
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Submit, Layout, Row, Column, Div, ButtonHolder, BaseInput, Hidden,
    Reset, Fieldset, Field, MultiField, MultiWidgetField, HTML
)
from .models import Comment
from django import forms
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.core.validators import (
    RegexValidator, EmailValidator, FileExtensionValidator
)
from django.contrib import messages


class ContactForm(forms.Form):
    nombre = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': _('nombre')}))
    asunto = forms.CharField(
        label="",widget=forms.TextInput(attrs={'placeholder': _('asunto') }))
    email = forms.EmailField(
        label="", widget=forms.EmailInput(attrs={'placeholder': _('example@gmail.com...')}), validators=[EmailValidator()])
    contenido = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': _('mensaje...')
        }),
    )
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'mb-3'})



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('foto','nombre','posicion','comentario',)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'rounded-0 mb-3'})
        self.fields["foto"].validators=[FileExtensionValidator(allowed_extensions=['jpg',])]


    