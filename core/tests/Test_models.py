import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):
    
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, self.filename)
        self.assertTrue(len(arquivo), len(self.filename))
        
class ServiceTestCase(TestCase):
    # aqui eu testo os metodos do model Servico

    def setUp(self):
        self.service = mommy.make('Service')    # coloco para criar uma instancia de service so para testar o 
                                                # str de service

    def test_str(self):
        self.assertEqual(str(self.service), self.service.service)

class PositionTestCase(TestCase):

    def setUp(self):
        self.position = mommy.make('Position')

    def test_str(self):
        self.assertEqual(str(self.position), self.position.position)

class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee = mommy.make('Employee')

    def test_str(self):
        self.assertEqual(str(self.employee), self.employee.name)