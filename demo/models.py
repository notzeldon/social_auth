from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import ugettext_lazy as _


class DemoUser(AbstractUser):

    receive_news = models.BooleanField(
        verbose_name=_('I want to receive news PlacePass news and offers')
    )

    email = models.EmailField(_('email address'), unique=True)
