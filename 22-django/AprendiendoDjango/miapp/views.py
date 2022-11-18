from django.shortcuts import render, HttpResponse,redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages
# Create your views here.
# MVC = Modelo Vista Controlador
# MVT = Modelo Template Vista -> en django a la Vista se le conoce como Template, y al Controlador como Vista

# A continuación se crea una variable que hará de template para poder tener un menú de páginas en todas las páginas, solo se agrega la variable layout a cada return
layout = """
<h1>Sitio Web con Django - Fernando Baculima</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de Pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
    <li>
        <a href="/template">Template</a>
    </li>
</ul>
<hr/>
"""

def index(request):

    #html = """        <h1>Inicio</h1>
    #  <p>Años pares hasta el 2050</p>
    #  <ul>
    #  """
    #year = 2021

    #while year <= 2050:
    #    if year % 2 == 0:
    #        html += f"<li>{str(year)}</li>"
    #    year += 1

    #html += '</ul>'
    titulo = 'Este es mi título'
    mi_dato = 'Soy un dato que está en la vista'

    #lista
    lenguajes = {'JavaScript', 'Python', 'Java'}

    #Para replicar el ejercicio de recorrer los años hasta 2050
    year = 2021
    hasta = range(year, 2051)

    return render(request, "index.html", {'titulo': titulo,
                                          'mi_variable':mi_dato,
                                          'lenguajes': lenguajes,
                                          'years': hasta,
                                          })

def hola_mundo(request):
    return render(request, "hola_mundo.html")


def pagina(request, redirigir=0):
    if redirigir==1:
            return redirect('/inicio/')

    if redirigir == 2:
        return redirect('/contacto/Fernando/Baculima')

    # Recomendable para controlar mejor la lógica, la llamada es por nombre de la ruta configurada en urls.py
    if redirigir == 3:
        return redirect('contacto',nombre='Juan', apellido='Perez')

    return render(request,"pagina.html")


# Respondiendo HTML sin utilizar plantillas
# Con parámetros opcionales, revisar los casos de rutas en ulrs.py
def contacto(request,nombre="",apellido=""):
    html=""
    if nombre and apellido:
        html = f"<h3>El nombre completo recibido es: {nombre} {apellido} </h3>"

    return HttpResponse(layout + f"""<h2>Información de Contacto </h2> <br/> {html} """)


# Enviando html desde templates
def template(request):
    return render(request, "index.html")


#Guardando artículos en la BD
def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    articulo.save()
    return HttpResponse(f"Articulo creado:  <strong>{articulo.title}</strong>  - {articulo.content}")


#Guardando artículos en la BD, esta vista recibe la data desde un formulario
def save_article(request):
    """ Con Get
    if request.method == 'GET':
        title = request.GET['title']
        content = request.GET['content']
        public = request.GET['public']
        articulo = Article(
        title = title,
        content = content,
        public = public,
        )
        articulo.save()
        return HttpResponse(f"Articulo creado:  <strong>{articulo.title}</strong>  - {articulo.content}")
    """
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title=title,
            content=content,
            public=public,
        )
        articulo.save()
        return HttpResponse(f"Articulo creado:  <strong>{articulo.title}</strong>  - {articulo.content}")
    else:
        return HttpResponse(f"El artículo No se ha creado")

def create_article(request):
    return render(request,'create_article.html')


def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']
            articulo = Article(
                title=title,
                content=content,
                public=public,
            )
            articulo.save()

            #Crear mensaje flash, una sesion que se muestra una sola vez
            messages.success(request,f'Has creado correctamente el artículo {articulo.id}')
            return redirect('articulos')

            #return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))
    else:
        formulario = FormArticle()

    return render(request,'create_full_article.html', {
        'form': formulario
    })



#Recuperando Artículos de la BD
def articulo(request):
    response = ''
    try:
        articulo = Article.objects.get(title="Segundo artículo", public=False)
        response = f"Articulo {articulo.title} - {articulo.content}"
    except Exception as e:
        response = f"Articulo No encontrado"

    return HttpResponse(response)


#Actualizando datos de un artículo en la BD
def editar_articulo(request,id):
    articulo = Article.objects.get(id=id)
    articulo.title = 'Articulo Editado'
    articulo.content = 'Este es otro contenido'
    articulo.public = False

    articulo.save()
    return HttpResponse(f"Artículo {articulo.id} editado")

def articulos(request):

    #recuperar todos, pero con orden
    #articulos = Article.objects.order_by('title')#con order

    #limit 3 elementos
    #articulos = Article.objects.order_by('title')[:2]

    #recuperar todos
    articulos = Article.objects.all()


    #Filtrando, lookups, algunos ejemplos
    # articulos = Article.objects.filter(title='Cuarto articulo')
    # articulos = Article.objects.filter(title='Cuarto articulo', id=3)     # AND
    articulos = Article.objects.filter(
            Q(title__contains='Primer') | Q(title__contains='otro')
    )  #                                                                    OR
    # articulos = Article.objects.filter(title__contains='Primer')          # Similar a Like
    # articulos = Article.objects.filter(title__exact='Primer')             # Coincidencia exacta
    # articulos = Article.objects.filter(title__iexact='Primer')            # Sin case sensitive
    # articulos = Article.objects.filter(id__gt=3)                          # Devuelve articulos cuyo id mayores a 3
    # articulos = Article.objects.filter(id__gte=3)                         # Devuelve articulos cuyo id mayores o igual a 3
    # articulos = Article.objects.filter(id__lt=3)                          # Devuelve articulos cuyo id menores o igual a 3
    # articulos = Article.objects.filter(id__lte=3)                         # Devuelve articulos cuyo id menores o igual a 3

    # Exclude
    # articulos = Article.objects.filter(
    #                     title__contains = 'articulo',
    # ).exclude(public=True)

    # UTILIZANDO SQL
    #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title like '%Cuarto%'")

    # recuperar todos
    articulos = Article.objects.filter(public='True')

    return render(request, 'articulos.html', {'articulos':articulos})

#Borrando artículos
def borrar_articulo(request, id):
    articulo = Article.objects.get(id=id)
    articulo.delete()

    return redirect('articulos')

