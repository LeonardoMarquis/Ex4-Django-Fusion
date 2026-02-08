from django.test import TestCase
from core.forms import ContactForm


class ContatoFormTestCase(TestCase):
    
    def setUp(self):
        self.nome = "Bonnie"
        self.email = "bonnie@example.com"
        self.assunto = "Informações sobre os serviços"
        self.mensagem = "Olá, gostaria de saber um pouco mais sobre os seus serviços."

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContactForm(data=self.dados)
    
    def test_send_mail(self):
        form1 = ContactForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEquals(res1, res2)