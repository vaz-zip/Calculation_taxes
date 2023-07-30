
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', include('allauth.urls')),
    # path('account_list', AccountList.as_view(), name='account_list'),
    # path('account_list/<int:pk>', AccountItem.as_view()),
    # path('account_list/<int:pk>/edit', EditAccount.as_view()),
    # path('account_list/create_account', CreateAccount.as_view(), name='create_account'),
]