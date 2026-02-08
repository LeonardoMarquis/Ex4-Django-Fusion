from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

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
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados) # para testar se a rota é valida, no caso estamos testando a form_valid la de enviar o email 
                                                                            # temos que acessar ela como o reverse_lazy e 
                                                                            # testar passar dados para ela logo
        self.assertEqual(request.status_code, 302)  # como a rota form_valid é quando envia o email e continua na pagina basica normal, o codigo http 302 é o certo a se esperar


    def test_form_invalid(self):    # nesse caso, para acontecer o metodo form_invalid, la nos defininmos que algum campo deveria esta errado
                                    # entao vamos fazer um errado aqui de proposito, como por ex: nao passar alguns campos
        self.dados = {
            'nome': self.nome,
            'email': self.email
        }

        request = self.cliente.post(reverse_lazy('index'), data=self.dados) # acessar a rota index e passar os dados no post, no caso, vai passar os dados justamente para o formulario da pagina index
                                                                    # ja que ele ja vem no ponto de so colocar as informacoes
        self.assertEqual(request.status_code, 200)  # no caso, estamos esperando que esse form_invalid de certo, e a condicao para ele dar certo nos ja garantimos, que é o form ter dados errados




