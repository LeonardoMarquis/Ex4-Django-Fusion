import uuid

from django.db import models
from stdimage.models import StdImageField

# para poder guardar as imagens com nomes unicos e prevenir que uma imgame tenha o mesmo nome de outra e sobtreponha
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]   # -1 para pegar a ultima parte do nome do arquivo apos o split
    filename = f'{uuid.uuid4()}.{ext}'  # o metodo uuid4 gera um id unico hexadecimal
    return filename


class Base(models.Model):
    created = models.DateTimeField('Created at', auto_now_add=True)     # guardar a data que foi criado
    modified = models.DateTimeField('Modified at', auto_now=True)          # atualizar a data sempre que salvar
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    # as nossas 6 opcoes de servicos na parte de servicos na nossa pagina index
    ICONE_CHOICES = (
        ('lni-cog', 'Engine'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Layers'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),  
    )

    service = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField('Position', max_length=100)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.position
    
class Employee(Base):
    name = models.CharField('Name', max_length=100)
    position = models.ForeignKey('core.Position', verbose_name='Position', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Image', upload_to= get_file_path, variations={
        'thumb': 
        {'width': 400, 
        'height': 400,
        'crop': True}})
    

    # se precisar recortar vai fazer esse crop automatico
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name= 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.name


