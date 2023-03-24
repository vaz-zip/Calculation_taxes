from django.urls import path
from .views import StaffList, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView, ChargesList, СhargesCreateView, \
                   СhargesDetailView, ChargesUpdateView, ChargesDeleteView  #doc_filter, , DocumentUpdateView, ImageDeleteView

from .models import Staff, Accruals_and_taxes

urlpatterns = [
    path('', StaffList.as_view(queryset=Staff.objects.all().order_by('surname'), template_name='staff.html'), name='staff'),
    path('<int:pk>', StaffDetailView.as_view(), name='worker'),
    path('create', StaffCreateView.as_view(), name='staff_add'),
    path('staff_edit/<int:pk>', StaffUpdateView.as_view(), name='staff_edit'),
    path('staff_delete/<int:pk>', StaffDeleteView.as_view(), name='staff_delete'),
    path('charge', ChargesList.as_view(queryset=Accruals_and_taxes.objects.all().order_by('payment_date', 'worker'), template_name='charges.html'), name='charge'),
    path('charges/<int:pk>', СhargesDetailView.as_view(), name='charges'),
    path('char_create', СhargesCreateView.as_view(), name='char_add'),
    path('charge_edit/<int:pk>', ChargesUpdateView.as_view(), name='char_edit'),
    path('charge_delete/<int:pk>', ChargesDeleteView.as_view(), name='char_delete'),

]