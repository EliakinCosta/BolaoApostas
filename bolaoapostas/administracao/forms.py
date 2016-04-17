from django import forms
from ajaximage.widgets import AjaxImageWidget
from .models import *
from django.contrib.admin import ModelAdmin

class AjaxImageUploadForm(forms.Form):
    
    images = forms.URLField(widget=AjaxImageWidget(upload_to='form-uploads'))
    

class MovimentacaoAdminForm(forms.ModelForm):
    
    class Meta:
        model = Movimentacao
        fields = '__all__'
    
    def clean(self):
        errors = {}
        if float(self.cleaned_data.get('valor')) <= 0:
            errors['valor'] = forms.ValidationError('Não é possível retirar créditos de um jogador', code='code')
            raise forms.ValidationError(errors)
            