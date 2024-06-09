from django import forms
from django.forms import TextInput

from accounts.models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль', strip=False, required=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль', strip=False,
                                       required=True)
    username = forms.CharField(max_length=300, label='Имя пользователя')
    email = forms.CharField(max_length=500, label='Адрес электронной почты', widget=TextInput(attrs={'type': 'email'}))
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = Account
        fields = ('avatar', 'username', 'email', 'first_name', 'last_name', 'bio', 'password', 'password_confirm',)


class AccountEditForm(forms.ModelForm):
    username = forms.CharField(max_length=300, label='Имя пользователя')
    email = forms.CharField(max_length=500, label='Адрес электронной почты', widget=TextInput(attrs={'type': 'email'}))
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)

    class Meta:
        model = Account
        fields = ('avatar', 'username', 'email', 'first_name', 'last_name', 'bio',)
