from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('full_name', 'status',)


class CustomUserChangeForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('full_name', 'status',)
