from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('scan_result',views.profile_view,name="scan_result"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('accounts/profile/', views.UserProfileView.as_view(), name="profile"),
    path('accounts/status/', views.UserStatusView.as_view(), name="status"),
]
