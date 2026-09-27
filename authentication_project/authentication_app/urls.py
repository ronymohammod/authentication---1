from django.urls import path
from authentication_app.views import *



urlpatterns = [
    path('register/',register_page, name='register_page'),
    path('login/', login_page, name="login_page"),
    path('logout/',logout_view,name="logout_view"),
    path('dashboard/',dashboard_page, name="dashboard_page"),
]