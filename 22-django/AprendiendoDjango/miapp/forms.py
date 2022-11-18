from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label = 'Titulo',
        max_length = 40,
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder':'Ingrese el título',
                'class' : 'title from article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es demasiado corto'),
            validators.RegexValidator('[A-Za-z0-9ñ]*$', 'El título está mal formado', 'Invalid Title'),
        ]
    )

    content = forms.CharField(
        label = 'Contenido',
        widget= forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20, 'La descripción es demasiado larga'),

        ]
    )

    #Otra forma de personalizar los atricutos del campo
    content.widget.attrs.update({
        'placeholder': 'Ingrese el contenido',
    })

    public_options = [
        (0, 'No'),
        (1, 'Si')
    ]
    public = forms.TypedChoiceField(
        label = 'Publicado?',
        choices = public_options
    )