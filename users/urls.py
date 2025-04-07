from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpPageView.as_view(), name='signup'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='edit_profile'),
]