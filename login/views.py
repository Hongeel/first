from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from .mixins import AjaxTemplateMixin

class Index(TemplateView):
    template_name = '/mainsite/index.html'

class CustomLoginView(AjaxTemplateMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
