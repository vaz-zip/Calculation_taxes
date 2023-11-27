from django_filters import FilterSet, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from django import forms
from .models import Staff, Accruals_and_taxes
# from taxes.resources import POSITIONS, POSITIONS_1, POSITIONS_2, y_2023, january, three_month, positions




class StaffFilter(FilterSet):
    class Meta:
        model = Staff
        fields = ('surname', 'ITN', 'post') 



class ChargesFilter(FilterSet):
    start_date = DateFilter(field_name='payment_date',
                                           widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='gt', label='Период выплат с  ')
    end_date = DateFilter(field_name='payment_date',
                                         widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                         lookup_expr='lt', label='по   ')
    
    date_range = ['start_date', 'end_date']
    
    class Meta:
        model = Accruals_and_taxes
        fields = ['worker']
      


class ReportFilter(FilterSet):
    start_date = DateFilter(field_name='reporting_date',
                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                            lookup_expr='gt', label='Период начисления с  ')
    end_date = DateFilter(field_name='reporting_date',
                          widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                          lookup_expr='lt', label='по   ')
    
    # end_date = '2023-09-01'
    
    

    # class Meta:
    #     model = Accruals_and_taxes
    #     fields = ['reporting_year']

    # def __str__(self):
    #     return f'{self.start_date}, {self.end_date}'
    # print  f'{self.start_date}, {self.end_date}'  
    


        
# print(dir(ReportFilter)) 