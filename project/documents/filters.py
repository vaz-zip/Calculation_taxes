from django_filters import FilterSet, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
import django.forms
from .models import Document
 
 
# создаём фильтр
class DocFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) 
    # информация о документаx
    dateCreate = DateFilter(widget=django.forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Document
        fields = ('title', 'category')
        # поля, которые мы будем фильтровать 
        # (т. е. отбирать по каким-то критериям, имена берутся из моделей)