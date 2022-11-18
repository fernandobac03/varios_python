from django.contrib import admin
from .models import Article, Category

# Register your models here.
# para mostrar campos de sololectura, como las fechas de creación y edición en el formulario del
# panel de django
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

# lo siguiente es realizado para poger gestionar mis módulos creados en mi app,
# desde el panel de administración de django

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configuracón para el TITULO DEL PANES
title = 'MASTER EN PYTHON - KD SOLUTIONS EC'
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "PANEL DE GESTIÓN"
