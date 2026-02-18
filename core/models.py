import uuid

from django.db import models
from stdimage.models import StdImageField

from django.utils.translation import gettext_lazy as _


# para poder guardar as imagens com nomes unicos e prevenir que uma imgame tenha o mesmo nome de outra e sobtreponha
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]   # -1 para pegar a ultima parte do nome do arquivo apos o split
    filename = f'{uuid.uuid4()}.{ext}'  # o metodo uuid4 gera um id unico hexadecimal
    return filename


class Base(models.Model):
    created = models.DateTimeField(_('Created at'), auto_now_add=True)     # guardar a data que foi criado
    modified = models.DateTimeField(_('Modified at'), auto_now=True)          # atualizar a data sempre que salvar
    active = models.BooleanField(_('Active?'), default=True)

    class Meta:
        abstract = True


class Service(Base):
    # as nossas 6 opcoes de servicos na parte de servicos na nossa pagina index
    ICONE_CHOICES = (
        ('lni-cog', _('Engine')),
        ('lni-stats-up', _('Graphic')),
        ('lni-users', _('Users')),
        ('lni-layers', _('Layers')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Rocket')),  
    )

    service = models.CharField(_('Service'), max_length=100)
    description = models.TextField(_('Description'), max_length=200)
    icon = models.CharField(_('Icon'), max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField(_('Position'), max_length=100)

    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')

    def __str__(self):
        return self.position
    
class Employee(Base):
    name = models.CharField(_('Name'), max_length=100)
    position = models.ForeignKey('core.Position', verbose_name=_('Position'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    image = StdImageField(_('Image'), upload_to= get_file_path, variations={
        'thumb': 
        {'width': 400, 
        'height': 400,
        'crop': True}})
    

    # se precisar recortar vai fazer esse crop automatico
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name= _('employee')
        verbose_name_plural = _('employees')

    def __str__(self):
        return self.name


