from django.test import TestCase

# Create your tests here.
def add_num(num):
    return num +1 

class simpleTestCase(TestCase):
    def setUp(self):
        print("Iniciando TesteCase")
    
    def test_add_num(self):
        valor = add_num(5)
        self.assertEqual(valor, 6)