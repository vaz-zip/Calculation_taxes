from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.conf import settings
from taxes.resources import POSITIONS, POSITIONS_1, POSITIONS_2, y_2023, january, three_month

# class Firm(models.Model): 
#     name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Фирма')

#     def __str__(self):
#         return f'{self.name}'

#     class Meta:
#         verbose_name = 'Фирма'
# class Author(User):
#     class Meta:
#         proxy = True

#     def __str__(self):
#         return self.first_name
    

class Staff(models.Model):
    # author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name='Автор')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Компания')
    surname = models.CharField(max_length=24, verbose_name='Фамилия')
    name = models.CharField(max_length=24, verbose_name='Имя')
    patronimic = models.CharField(max_length=24, blank=True, verbose_name='Отчество')
    ITN = models.IntegerField(unique=True, verbose_name='ИНН')
    post = models.CharField(max_length=24, verbose_name='Должность')
    dependents = models.IntegerField(default=0, verbose_name='Дети')
    description = models.TextField(max_length=150, blank=True, verbose_name='Описание')
    class Meta:
        ordering = ['surname']
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Персонал'

    def __str__(self):
        return f'{self.surname} {self.name}'
    

    def get_absolute_url(self):
        return f'/{self.id}'


class Accruals_and_taxes(models.Model):
    # class Reporting(models.TextChoices):

    # author = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')
    worker = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Работник')
    reporting_year = models.CharField(max_length=4, choices=POSITIONS, default="2023", verbose_name='Год')
    # reporting_quarter = models.CharField(max_length=6, choices=POSITIONS_1, default='3 мес.', verbose_name='Квартал')
    # reporting_month = models.CharField(max_length=4, choices=POSITIONS_2, default='ЯНВ', verbose_name='Месяц')
    payment_date = models.DateField(verbose_name='Дата выплаты')
    reporting_date = models.DateField(verbose_name='Дата начисления')
    accrued = models.FloatField(verbose_name='Начислено')
    alimony = models.FloatField(default=0, verbose_name='Коэфф.Ал')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.worker}'

    class Meta:
        verbose_name = 'Начисления'

    def social_deductions(self):
        dependents = self.worker.dependents
        if dependents <= 2:
            return dependents * 1400
        elif dependents >= 3:
            return 2800 + (3000 * int(dependents - 2))
        else:
            return dependents == 0

    def income_tax(self):
        accrued = self.accrued
        social_deductions = self.social_deductions()
        return (accrued - social_deductions) * 0.13

    def alimony_tax(self):
        accrued = self.accrued
        alimony = self.alimony
        return accrued * alimony

    def salary(self):
        accrued = self.accrued
        alimony_tax = self.alimony_tax()
        income_tax = self.income_tax()
        return accrued - (alimony_tax + income_tax)

    def single_tax(self):
        accrued = self.accrued
        return accrued * 0.3

    def injury_insurance(self):
        accrued = self.accrued
        return accrued * 0.004
    

    def t_sum(self):
        sum_acr = Accruals_and_taxes.objects.aggregate(Sum('accrued')).get('accrued__sum')
        return sum_acr
    
    
    def __str__(self):
        return f'{self.accrued}'

                #Accruals_and_taxes.objects.aggregate(Sum('accrued'))
        # summ = Accruals_and_taxes.objects.all()
#  {% for accruals_and_taxes in taxes %}
#                                                    {{ accruals_and_taxes.accrued }       
    # def single_tax_sum(self):
    #     accrued = self.accrued
    #     accruals_and_taxes = Accruals_and_taxes()
    #     accrued = i

    #     for i  in accruals_and_taxes:
    #         i = i + i
    #         return i * 0.3

    #     field_name_sum = Accruals_and_taxes.objects.aggregate(Sum('accrued'))

        # print(my_dict.get('Возраст'))
        # for k, v in field_name_sum.items():
        # return field_name_sum.get('accrued_sum')
        # S = 0
        # single_tax = self.single_tax()
        # for vol in single_tax:
        #     S = S + vol
        #     return S

    class Meta:
        verbose_name = 'Выплаты'
        verbose_name_plural = 'Суммы выплат'

    def get_absolute_url(self):
        return f'/charges/{self.id}'


# def t_sum(self):
#     # accrued = self.accrued
#     sum = Accruals_and_taxes.objects.aggregate(Sum('accrued'))
#         # summ = Accruals_and_taxes.objects.all()
#     return sum