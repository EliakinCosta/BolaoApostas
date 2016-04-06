from django import forms
from ajaximage.widgets import AjaxImageWidget

class AjaxImageUploadForm(forms.Form):
    images = forms.URLField(widget=AjaxImageWidget(upload_to='form-uploads'))