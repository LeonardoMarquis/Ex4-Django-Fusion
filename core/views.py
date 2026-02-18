from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, FormView

from .models import Service, Employee
from .forms import ContactForm

from django.utils.translation import gettext as _
from django.utils import translation

'''class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.all()

        return context'''

class IndexView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        lang = translation.get_language()

        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.all()

        context['lang'] = lang          # essa variavel de contexto é para poder essa variavel ir para o template base.html e funcioanr como uma vairavel la, no caso atribui o valor dela como a lang que peguei anteriormente
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, _('Message sent successfully!'))     # ficou muito facil usar o metode de get text colocando ele como um _
        
        # o metodo gettext é para considerar o txto dentro como se fosse "texto passivel de traducao"

        return super().form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Error sending message. Please try again.'))
        
        return super().form_invalid(form, *args, **kwargs)




class TesteView(TemplateView):
    template_name = "teste.html"