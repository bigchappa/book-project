from django.template import context
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from . import forms
from . import models

# Create your views here.
class SignUpPageView(CreateView):

    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class ProfileDetailView(DetailView):

    model = models.UserProfile
    template_name = 'account/profile.html'

    def get_object(self, queryset = ...):
        
        profile, created = models.UserProfile.objects.get_or_create(
            user=self.request.user,
        )

        return profile
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object()
        context['books'] = self.get_object().books.all()

        return context
        
class ProfileEditView(UpdateView):
    
    model = models.UserProfile
    form_class = forms.UserProfileForm
    template_name = 'account/change_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset = ...):
        
        profile, created = models.UserProfile.objects.get_or_create(
            user=self.request.user,
        )

        return profile

