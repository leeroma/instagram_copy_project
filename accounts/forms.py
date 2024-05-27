from django import forms

from accounts.models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль', strip=False, required=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль', strip=False,
                                       required=True)

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
        fields = ('avatar', 'username', 'email', 'first_name', 'last_name', 'password', 'password_confirm', )


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'password', )
