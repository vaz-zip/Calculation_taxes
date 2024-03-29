from django.shortcuts import render, redirect
from django_filters import FilterSet, DateFilter
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Staff, Accruals_and_taxes
from .filters import StaffFilter, ChargesFilter, ReportFilter
from .forms import StaffCreateForm, ChargesCreateForm


class StaffList(LoginRequiredMixin, ListView):
    model = Staff
    template_name = 'staff.html'
    context_object_name = 'staff'
    queryset = Staff.objects.all()
    filter_class = StaffFilter
    paginate_by = 3

    def get_queryset(self):
        self.filter = self.filter_class(self.request.GET, super().get_queryset().filter(author_id=self.request.user.id))
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StaffFilter(self.request.GET, queryset=self.get_queryset())
        return context


class StaffDetailView(LoginRequiredMixin, DetailView):
    model = Staff
    template_name = 'employee.html'
    context_object_name = 'staff'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Staff.objects.get(pk=id)


class StaffCreateView(LoginRequiredMixin, CreateView):
    template_name = 'staff_add.html'
    form_class = StaffCreateForm

    def get_success_url(self) -> str:
        return '/staff'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            Staff.objects.create(**(form.cleaned_data) | {'author': request.user})
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'edit_staff.html'
    form_class = StaffCreateForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Staff.objects.get(pk=id)


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    template_name = 'delete_staff.html'
    context_object_name = 'staff'
    success_url = '/staff'


class ChargesList(LoginRequiredMixin, ListView):
    model = Accruals_and_taxes
    template_name = 'charges.html'
    # single_tax_sum = Accruals_and_taxes.objects.aggregate(Sum('accrued'))
    context_object_name = 'accruals_and_taxes'
    filter_class = ChargesFilter
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #     # context['time_now'] = datetime.now()
        #  context['list_in_page'] = self.paginate_by
        context['staff'] = Staff.objects.all()
        context['filter'] = ChargesFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        # f = Staff.objects.all(user = self.request.user)
        self.filter = self.filter_class(self.request.GET, super().get_queryset())  # .filter(f))
        return self.filter.qs.all()


class FinreportList(LoginRequiredMixin, ListView):
    model = Accruals_and_taxes
    template_name = 'report.html'
    filter_class = ReportFilter
    context_object_name = 'taxes'

    def get_queryset(self):
        self.filter = self.filter_class(self.request.GET, super().get_queryset())
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        self.filter = self.filter_class(self.request.GET, queryset=self.get_queryset())
        context = super().get_context_data(**kwargs)
        context['filter'] = ReportFilter(self.request.GET, queryset=self.get_queryset())
        c = self.request # получение запроса
        print(c) # внешний вид запроса
        d = self.request.GET # получаем параметры запроса (ключ: знчение)
        print(d)
        print(d.get('start_date'))
        print(d.get('end_date'))        
        start_date = self.request.GET.get('start_date') # получаем переменную start_date
        end_date = d.get('end_date') # получаем переменную end_date
        processed_request = Accruals_and_taxes.objects.filter(reporting_date__range = (start_date, end_date)) # находим отфильтрованные по дате ключ: значение словаря QuerySet 
        # print(processed_request)
        
        
        def summ_accrued():
            summ = 0
            for item in processed_request.values('accrued'): # получаем начислеия за период
                for accrued in item.values():                
                    for i in [accrued]:                      # получаем сумму начислений за период
                        summ += i
            return summ
        context['summ'] = summ_accrued                       # контекст суммы начислений


        def summ_alimony():
            summ = 0
            for item in processed_request:
                # print(item.worker, item.alimony)
                for i in [item.alimony]:
                    summ += i
            return summ
        context['summ_al'] = summ_alimony  


        def sum_income_tax():
            summ = 0
            for item in processed_request:
                print(item.worker, item.accrued, (item.accrued) * 0.13)
                for i in [item.accrued * 0.13]:
                    summ += i
            return summ
        context['summ_inc_tax'] = sum_income_tax


        def sum_salary():
            summ = 0
            for item in processed_request:
                print(item.worker, item.accrued - item.accrued * 0.13)
                for i in [item.accrued - item.accrued * 0.13]:
                    summ += i
            return summ
        context['summ_salary'] = sum_salary


        def sum_singl_tax():
            summ = 0
            for item in processed_request:
                print(item.worker, item.accrued * 0.3)
                for i in [item.accrued * 0.3]:
                    summ += i
            return summ
        context['summ_singl_tax'] = sum_singl_tax

        def sum_injury_insurance():
            summ = 0
            for item in processed_request:
                print(item.worker, item.accrued * 0.004)
                for i in [item.accrued * 0.004]:
                    summ += i
            return summ
        context['summ_injury_insurance'] = sum_injury_insurance



        
        # int_sum = float(context['summ'])
        # print(int_sum * 0.0010)
        # context['single_tax'] = int_sum * 0.3
        # context['injury_insurance'] = int_sum * 0.004
        # context['soc'] = Accruals_and_taxes.objects.filter(reporting_date__range = (start_date, end_date)).aggregate(Sum('social_deductions')).get('social_deductions')
        return context
    


class СhargesDetailView(DetailView):
    model = Accruals_and_taxes
    template_name = 'charges_detail.html'
    context_object_name = 'accruals_and_taxes'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Accruals_and_taxes.objects.get(pk=id)


class СhargesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'charges_add.html'
    form_class = ChargesCreateForm

    def get_success_url(self) -> str:
        return '/charge'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            Accruals_and_taxes.objects.create(**(form.cleaned_data))  # | {'worker': request.user})
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    # def project_document_add(request, id):
    # project = Project.objects.get(id=id)
    # if request.POST:
    #     form = DocumentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('projectinfo', id)
    # org = ProjectCompany.objects.filter(project=project)
    # context = {
    #     'form': DocumentForm(initial={'project': project, 'organization': org}),
    #     'project': project
    # }
    # return render(request, 'documents/projectdocumentadd.html', context)


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
