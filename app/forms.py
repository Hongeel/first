from django import forms
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms.widgets import EmailInput
from django.contrib.auth.forms import AuthenticationForm


from .validate import validate_bio, validate_date

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class UserAccountCreationForm(UserCreationForm):

    verify_email = forms.EmailField(label="Verify your email")

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'email', 'verify_email'
        )

    def __init__(self, *args, **kwargs):
        '''Note: A user defined field needs a label argument
        passed to the field constructor in order for a placeholder
        to render properly in HTML'''

        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})

    def clean_verify_email(self):
        my_email = self.cleaned_data['email']
        verify_email = self.cleaned_data['verify_email']

        if my_email != verify_email:
            msg = "Email doesn't match the previously entered email."
            raise ValidationError(msg)


class ProfileForm(forms.ModelForm):

    birth = forms.DateField(label="Date of birth", validators=[validate_date])
    bio = forms.CharField(label="Your bio...", validators=[validate_bio], widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ('birth', 'bio', 'avatar')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})


class EditUserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})

    def clean_verify_email(self):
        my_email = self.cleaned_data['email']
        verify_email = self.cleaned_data['verify_email']

        if my_email != verify_email:
            msg = "Email doesn't match the previously entered email."
            raise ValidationError(msg)