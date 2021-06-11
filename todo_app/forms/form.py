from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinLengthValidator


def validate_name(value):
    if not value[0].isupper() \
            or len(value) < 6:
        raise ValidationError("The name must start with an uppercase letter.")


def validate_age(value):
    if value < 0:
        raise ValidationError("The age cannot be less than zero.")


def validate_email(value):
    EmailValidator(value)


def validate_password(value):
    MinLengthValidator(8)(value)
    for char in value:
        if not char.isalnum():
            raise ValidationError("Enter a valid password.")


class UserForm(forms.Form):
    name = forms.CharField(
        validators=[validate_name],
    )
    age = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[validate_age],
    )
    email = forms.EmailField(
        widget=forms.EmailInput,
        validators=[validate_email],
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[validate_password],
    )
    text = forms.CharField(
        widget=forms.Textarea
    )
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )


    def clean_bot_catcher(self):
        bot_catcher = self.cleaned_data['bot_catcher']
        if len(bot_catcher) > 0:
            raise forms.ValidationError("You are a bot!")


    def cleaned_password(self):
        pure_pass = self.cleaned_data['password']
        return f'!@#{pure_pass}!@#'