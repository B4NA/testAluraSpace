from django.urls import path
from users.views import login, logon, logout

urlpatterns = [
    path('login', login, name='login'),
    path('logon', logon, name='logon'),
    path('logout', logout, name='logout'),
]