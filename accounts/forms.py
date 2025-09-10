from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        """Save the user ensuring both username and email are set to the provided email.
        We intentionally collect email in the "username" field to allow email-based login
        with Django's default AuthenticationForm. This method mirrors that value to
        the actual User.email field so the DB column is populated and normalizes the email to lowercase.
        """
        user = super().save(commit=False)
        email = self.cleaned_data.get("username", "").strip().lower()
        if email:
            user.username = email
            user.email = email
        if commit:
            user.save()
        return user