from django_filters import FilterSet, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from django import forms
from .models import Document
 
 
# создаём фильтр
class DocFilter(FilterSet):
    #Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) 
    # информация о документаx
    start_date = DateFilter(field_name='dateCreate',
                                           widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='gt', label='Внесён в базу с  ')
    end_date = DateFilter(field_name='dateCreate',
                                         widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                         lookup_expr='lt', label='по   ')
   
    class Meta:
        model = Document
        fields = ['category']
