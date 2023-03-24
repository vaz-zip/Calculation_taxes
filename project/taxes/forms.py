from django import forms
from .models import Staff, Accruals_and_taxes

from django.contrib.auth.models import User


class StaffCreateForm(forms.ModelForm):
    # images = forms.ImageField(label='Фото документа', widget=forms.ClearableFileInput(attrs={'multiple': True, "class":"mybottom"}))

    class Meta:
        model = Staff
        # widgets = {
        #     'dateCreate': forms.DateInput(attrs={'type': 'date'}),
        # }widgets = {'project': forms.HiddenInput()}
        # # {
        # #     'author': request.user.username
        # # }

        fields = ['surname', 'name', 'patronimic', 'post', 'ITN', 'dependents', 'description']


class ChargesCreateForm(forms.ModelForm):

    class Meta:
        model = Accruals_and_taxes
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'})}
        fields =[
            'worker', 'payment_date', 'reporting_year', 'reporting_quarter', 'reporting_month',
                'accrued', 'alimony', 'description']