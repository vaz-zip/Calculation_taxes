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

    # def __init__(self, *args, **kwargs):
    #      super(ChargesCreateForm, self).__init__(*args, **kwargs)
    #      self.fields['worker'].queryset = Staff.objects.filter(author_id=self.user.id)

    class Meta:
        model = Accruals_and_taxes
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'})}
        fields =[
            'worker', 'payment_date', 'reporting_year', 'reporting_quarter', 'reporting_month',
                'accrued', 'alimony', 'description']
        

# class DocumentForm(forms.ModelForm):
#     def __init__(self, project, *args, **kwargs):
#         super(DocumentForm, self).__init__(*args, **kwargs)
#         self.fields['organization'].queryset = Company.objects.filter(projectcompany__project=project)

#     class Meta:
#         model = Documents
#         fields = ('__all__')        