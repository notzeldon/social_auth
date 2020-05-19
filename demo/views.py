from http.cookiejar import request_host

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views import generic

from demo.forms import RegisterForm


class DemoTemplateView(generic.TemplateView):
    template_name = 'demo.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['form'] = RegisterForm()

        return ctx


class DemoRegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')
