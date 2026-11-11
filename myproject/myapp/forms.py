from django import forms
from django.contrib.auth.hashers import make_password

from .models import Student


class StudentForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        strip=False,
        min_length=8,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        strip=False,
    )

    class Meta:
        model = Student
        fields = ("name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["autocomplete"] = {
                "name": "name",
                "email": "email",
                "password": "new-password",
                "confirm_password": "new-password",
            }[field_name]
        if self.instance.pk is None:
            self.fields["password"].required = True
            self.fields["confirm_password"].required = True

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password or confirm_password:
            if password != confirm_password:
                self.add_error("confirm_password", "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        student = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            student.password_hash = make_password(password)
        if commit:
            student.save()
            self.save_m2m()
        return student
