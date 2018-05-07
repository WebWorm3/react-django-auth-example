from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('auth/', views.auth_view, name='auth_view'),
    path('user_data/', views.get_user_data, name='get_user_data'),
]
