from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views import generic


class DemoTemplateView(generic.TemplateView):
    template_name = 'demo.html'


def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')
