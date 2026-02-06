from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, FormView

from .models import Service, Employee
from .forms import ContactForm


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
        context['services'] = Service.objects.all()
        context['employees'] = Employee.objects.all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'Message sent successfully!')
        
        return super().form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error sending message. Please try again.')
        
        return super().form_invalid(form, *args, **kwargs)




class TesteView(TemplateView):
    template_name = "teste.html"