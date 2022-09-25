from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class MyauthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={"autofocus": True, 'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(
        label=("Password:"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'class': 'input', 'placeholder': 'Password'}),
    )
