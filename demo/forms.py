from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import EmailField
from django import forms

from django.utils.translation import ugettext_lazy as _

from demo.models import DemoUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("last_name", "first_name", "email",)
        field_classes = {'email': EmailField }
        
    receive_news = forms.BooleanField(
        label=_('I want to receive news PlacePass news and offers'),
        widget=forms.CheckboxInput,
        required=False,
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.username:
            user.username = 'user_%d' % get_user_model().objects.all().count()
        user.receive_news = self.cleaned_data['receive_news']
        if commit:
            user.save()

        print(user)
        return user

