from django.urls import path
from . import views

app_name='dashboard'

urlpatterns = [
    path('awner-login-xs3/', views.admin_login, name='login'),
    path('dashboardhome/', views.admin_home, name='home'),
    path('logout/', views.admin_logout, name='logout'),
    path(
    "orders/<int:order_id>/status/",
    views.update_order_status,
    name="update_order_status",
),
]