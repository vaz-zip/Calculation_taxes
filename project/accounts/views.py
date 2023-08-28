
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
# from .forms import *
# from silant.models import Service_company


# class AccountList(PermissionRequiredMixin, ListView):
#     permission_required = 'auth.view_user'
#     model = User
#     template_name = 'account_list.html'
#     context_object_name = 'users'

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         order_by = self.request.GET.get('order_by', 'first_name')
#         context['users'] = User.objects.order_by(order_by)
#         return context