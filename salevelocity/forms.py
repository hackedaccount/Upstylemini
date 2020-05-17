from django import forms

from django.conf import settings
from salevelocity import models
import datetime


class SaleVelocityForm(forms.ModelForm):
    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget)
    end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget,
                               initial=datetime.date.today())
    download = forms.BooleanField(required=False)

    class Meta:
        model = models.SaleVelocity
        fields = ['datetime']
