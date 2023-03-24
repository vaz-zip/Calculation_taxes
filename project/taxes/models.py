from django.db import models
from django.contrib.auth.models import User
from taxes.resources import POSITIONS, POSITIONS_1, POSITIONS_2, y_2023, january, three_month

# class Firm(models.Model): ПОКА НЕ ПОДКЛЮЧЕН!!!!!!БУДЕТ НУЖЕН!!!!!
#     name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Фирма')

#     def __str__(self):
#         return f'{self.name}'

#     class Meta:
#         verbose_name = 'Фирма'


class Staff(models.Model):
    surname = models.CharField(max_length=24, verbose_name='Фамилия')
    name = models.CharField(max_length=24, verbose_name='Имя')
    patronimic = models.CharField(max_length=24, blank=True, verbose_name='Отчество')
    ITN = models.IntegerField(unique=True, verbose_name='ИНН')
    post = models.CharField(max_length=24, verbose_name='Должность')
    dependents = models.IntegerField(default=0, verbose_name='Дети')
    description = models.TextField(
        max_length=50, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Персонал'

    def get_absolute_url(self):
        return f'/{self.id}'
    


class Accruals_and_taxes(models.Model):
    worker = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Работник')
    reporting_year = models.CharField(max_length=4, choices=POSITIONS, default=y_2023, verbose_name='Год')
    reporting_quarter = models.CharField(max_length=6, choices=POSITIONS_1, default=three_month, verbose_name='Квартал')
    reporting_month = models.CharField(max_length=4, choices=POSITIONS_2, default=january, verbose_name='Месяц')
    payment_date = models.DateField(verbose_name='Дата выплаты')
    accrued = models.FloatField(verbose_name='Начислено')
    # _social_deductions = models.FloatField(default=0, db_column='social_deductions', verbose_name='Соц. вычет')
    alimony = models.FloatField(default=0, verbose_name='Коэфф.Ал')
    # _income_tax = models.FloatField(default=0, db_column='income_tax', verbose_name='НДФЛ')
    # _salary = models.FloatField(default=0, db_column='salary', verbose_name='Выдано')
    # _single_tax = models.FloatField(default=0, db_column='single_tax', verbose_name='Единый налог')
    # _injury_insurance = models.FloatField(default=0, db_column='injury insurance', verbose_name='Страховой взнос')
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

    def __str__(self):
        return f'{self.accrued}'

    class Meta:
        verbose_name = 'Выплаты'
        verbose_name_plural = 'Суммы выплат'


    def get_absolute_url(self):
        return f'/charges/{self.id}'    
