from django import forms

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class UserForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "username",
                "id": "username",
                "placeholder": "Kullanıcı adınız",
            }
        ),
    )

    password = forms.CharField(

        min_length=5,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "id": "password",
                "placeholder": "Parolanız",
            }
        ),
    )

    repassword = forms.CharField(

        min_length=5,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "repassword",
                "id": "repassword",
                "placeholder": "Parola tekrarı",
            }
        ),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def clean(self):
        cleaned_data = super().clean()
        captcha_value = cleaned_data.get("captcha")
        if not captcha_value:
            raise forms.ValidationError("Captcha doğrulama hatası")
        return cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "username",
                "id": "username",
                "placeholder": "Kullanıcı adınız",
            }
        ),
    )

    password = forms.CharField(

        min_length=5,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "id": "password",
                "placeholder": "Parolanız",
            }
        ),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def clean(self):
        cleaned_data = super().clean()
        captcha_value = cleaned_data.get("captcha")
        if not captcha_value:
            raise forms.ValidationError("Captcha doğrulama hatası")
        return cleaned_data


class CommentForm(forms.Form):
    comment = forms.CharField(
        min_length=5,
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "name": "content",
                "id": "content",
                "placeholder": "Mesajınız",
            }
        ),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def clean(self):
        cleaned_data = super().clean()
        captcha_value = cleaned_data.get("captcha")
        if not captcha_value:
            raise forms.ValidationError("Captcha doğrulama hatası")
        return cleaned_data
