from . import models
from django import forms

class ReviewAddForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ('review', )
