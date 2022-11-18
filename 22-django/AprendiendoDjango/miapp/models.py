from django.db import models

# Create your models here.
#verbose_name, utilizado para cambiar el nombre que se deseq v isualizar en el panel de administración
#ademas django detecta el lenguaje y modifica otras etiquetas para que se visualicen en espanol

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',upload_to='articles', verbose_name="Imagen")
    public = models.BooleanField(verbose_name="Publicado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    #para modificar los nombres que se visualizaran en el panel de admin de django
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-id']


    #para imprimir los objetos (en el panel de admin de django) de una manera legible
    def __str__(self):
        if self.public:
            publico = '(publicado)'
        else:
            publico = '(privado)'
        return f"{self.title}  - {publico}"


class Category(models.Model):
    name = models.CharField(max_length = 110)
    description = models.CharField(max_length = 250)
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
