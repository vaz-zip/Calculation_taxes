from django_filters import FilterSet, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
import django.forms
from .models import Staff, Accruals_and_taxes
# from taxes.resources import POSITIONS, POSITIONS_1, POSITIONS_2, y_2023, january, three_month, positions




class StaffFilter(FilterSet):
    class Meta:
        model = Staff
        fields = ('surname', 'ITN', 'post') 



class ChargesFilter(FilterSet):
    payment_date = DateFilter(widget=django.forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Accruals_and_taxes
        fields = ('worker', 'payment_date')
        


class ReportFilter(FilterSet):
    class Meta:
        model = Accruals_and_taxes
        fields = ('reporting_month', 'reporting_quarter', 'reporting_year')   