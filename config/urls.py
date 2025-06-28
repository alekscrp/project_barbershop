from django.contrib import admin
from django.urls import path, include
from core.views import landing, thanks, orders_list, order_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mainapp.urls")),
    path("", landing, name="landing"),
    path("thanks/", thanks, name="thanks"),
    path("orders/", orders_list, name="orders_list"),
    path("orders/<int:order_id>/", order_detail, name="order_detail"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
]
