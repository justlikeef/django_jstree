from django.contrib import admin
from django_jstree.models.jstree import jstree
from django_jstree.models.nodeType import nodeType
from django_jstree.models.popupMenuItem import popupMenuItem
from django_jstree.models.popupMenuItem import nodeTypePopupMenuItem

class nodeTypePopupMenuItemInline(admin.TabularInline):
    model = nodeTypePopupMenuItem

class nodeTypeAdmin(admin.ModelAdmin):
    inlines = (nodeTypePopupMenuItemInline,)

class popupMenuItemAdmin(admin.ModelAdmin):
    inlines = (nodeTypePopupMenuItemInline,)

# Register your models here.
admin.site.register(jstree)
admin.site.register(nodeType, nodeTypeAdmin)
admin.site.register(popupMenuItem, popupMenuItemAdmin)
