from django_filters import FilterSet #, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
import django.forms
from .models import Staff, Accruals_and_taxes




class StaffFilter(FilterSet):
    class Meta:
        model = Staff
        fields = ('surname', 'ITN', 'post') 



class ChargesFilter(FilterSet):
    class Meta:
        model = Accruals_and_taxes
        fields = ('worker', 'payment_date')
        


class ReportFilter(FilterSet):
    class Meta:
        model = Accruals_and_taxes
        fields = ('reporting_month', 'reporting_quarter', 'reporting_year')   