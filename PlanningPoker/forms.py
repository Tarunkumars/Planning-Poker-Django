from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from PlanningPoker.models import Game


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }


class GameForm(ModelForm):
    class Meta:
        model = Game
        players = forms.ModelMultipleChoiceField(queryset=User.objects.all())
        fields = ['name', 'players']
        # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        # widgets = {
        #     'players': forms.ChoiceField(widget=forms.SelectMultiple, choices=['ssdf','ffff']),
        # }