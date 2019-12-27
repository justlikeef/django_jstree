from django.contrib import admin
from django_jstree.models.jstree import jstree
from django_jstree.models.nodeType import nodeType

# Register your models here.
admin.site.register(jstree)
admin.site.register(nodeType)
