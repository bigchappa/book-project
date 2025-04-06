from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUpPageView(CreateView):

    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'