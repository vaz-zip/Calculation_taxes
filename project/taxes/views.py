from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #, w, RedirectView
from .models import Staff, Accruals_and_taxes
from .filters import StaffFilter, ChargesFilter, ReportFilter
from .forms import StaffCreateForm, ChargesCreateForm


class StaffList(ListView):
    model = Staff
    template_name = 'staff.html'
    context_object_name = 'staff'
    queryset = Staff.objects.all()
    filter_class = StaffFilter  # вновь
    paginate_by = 3

    def get_queryset(self):
        # .filter(author_id=self.request.user.id))
        self.filter = self.filter_class(self.request.GET, super().get_queryset())
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #     # context['time_now'] = datetime.now()
     #  #  context['list_in_page'] = self.paginate_by
        context['filter'] = StaffFilter(self.request.GET, queryset=self.get_queryset())
        return context


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'employee.html'
    context_object_name = 'staff'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Staff.objects.get(pk=id)


class StaffCreateView(CreateView):
    template_name = 'staff_add.html'
    form_class = StaffCreateForm

    def get_success_url(self) -> str:
        return '/'


class StaffUpdateView(UpdateView):
    template_name = 'edit_staff.html'
    form_class = StaffCreateForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Staff.objects.get(pk=id)


class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'delete_staff.html'
    context_object_name = 'staff'
    success_url = '/'



class ChargesList(ListView):
    model = Accruals_and_taxes
    template_name = 'charges.html'
    context_object_name = 'accruals_and_taxes'
    filter_class = ChargesFilter
    paginate_by = 3

    def get_queryset(self):
        # .filter(author_id=self.request.user.id))
        self.filter = self.filter_class(self.request.GET, super().get_queryset())
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #     # context['time_now'] = datetime.now()
       #  context['list_in_page'] = self.paginate_by
        context['filter'] = ChargesFilter(self.request.GET, queryset=self.get_queryset())
        return context
    

class FinreportList(ListView):
    model = Accruals_and_taxes
    template_name = 'report.html'
    context_object_name = 'accruals_and_taxes'
    filter_class = ReportFilter
    # paginate_by = 3

    def get_queryset(self):
        # .filter(author_id=self.request.user.id))
        self.filter = self.filter_class(self.request.GET, super().get_queryset())
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #     # context['time_now'] = datetime.now()
       #  context['list_in_page'] = self.paginate_by
        context['filter'] = ReportFilter(self.request.GET, queryset=self.get_queryset())
        return context
    


class СhargesDetailView(DetailView):
    model = Accruals_and_taxes
    template_name = 'charges_detail.html'
    context_object_name = 'accruals_and_taxes'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Accruals_and_taxes.objects.get(pk=id)
    

class СhargesCreateView(CreateView):
    template_name = 'charges_add.html'
    form_class = ChargesCreateForm

    def get_success_url(self) -> str:
        return '/charge'
    

class ChargesUpdateView(UpdateView):
    template_name = 'charges_edit.html'
    form_class = ChargesCreateForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Accruals_and_taxes.objects.get(pk=id)
    

class ChargesDeleteView(DeleteView):
    model = Accruals_and_taxes
    template_name = 'charge_delete.html'
    context_object_name = 'accruals_and_taxes'
    success_url = '/charge'
