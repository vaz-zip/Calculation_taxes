from django.contrib import admin
from .models import Staff, Accruals_and_taxes


class StaffAdmin(admin.ModelAdmin):
    fields = ['surname', 'name', 'patronimic', 'post', 'ITN', 'dependents']
    list_display = ['author_id', 'id', 'surname', 'name', 'patronimic',
                    'post', 'ITN', 'dependents', 'description']

    def get_queryset(self, obj):
        return Staff.objects.all().order_by('surname')


class Accruals_and_taxesAdmin(admin.ModelAdmin):
    fields = ['worker', 'accrued', 'reporting_year', 'reporting_quarter',
              'reporting_month', 'payment_date', 'description', 'alimony']
    list_display = ['worker', 'payment_date', 'reporting_year', 'reporting_quarter', 'reporting_month', 'accrued', 'social_deductions',
                    'alimony', 'alimony_tax', 'income_tax', 'salary', 'single_tax', 'injury_insurance', 'description', 'worker_id']

    def get_queryset(self, obj):
        return Accruals_and_taxes.objects.all().order_by('payment_date', '-worker')


admin.site.register(Staff, StaffAdmin)
admin.site.register(Accruals_and_taxes, Accruals_and_taxesAdmin)
