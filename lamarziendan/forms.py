from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.text import slugify
from .models import TeamMember

username_validator = UnicodeUsernameValidator()

class SignupForm(forms.Form):
    secret_code = forms.CharField(label='SUPERGEHEIME CODE', max_length=16)
    first_name = forms.CharField(label='Voornaam', max_length=30)
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Gebruikersnaam', max_length=150)
    password = forms.CharField(label='Wachtwoord', max_length=32, widget=forms.PasswordInput)

    def clean_secret_code(self):
        secret_code = self.cleaned_data['secret_code']
        if secret_code != 'ikwaserbij':
            self.add_error('username', 'Sorry, deze code is niet geldig')
        return secret_code

    def clean_username(self):
        username = self.cleaned_data['username']
        username_validator(username)
        if get_user_model().objects.filter(username=username).exists():
            self.add_error('username', 'Helaas, deze gebruikersnaam is al bezet')
        else:
            return username

    def save(self):
        first_name = self.cleaned_data['first_name']
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = get_user_model()(username=username, first_name=first_name, email=email, is_staff=True)
        user.set_password(password)
        user.save()

        try:
            group = Group.objects.get(name='Kernteam')
            user.groups.add(group)
            TeamMember(name=first_name, slug=slugify(first_name)).save()
        except:
            pass

        return user
