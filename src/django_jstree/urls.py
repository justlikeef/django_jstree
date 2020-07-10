from django.contrib import admin
from django.urls import path
from django_jstree.views import jsTree
from django_jstree.views import jsTreeByName
from django_jstree.views import NodeAsJSONJSTree

urlpatterns = [
    path('django_jstree/shownode/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>/<int:nodeid>', NodeAsJSONJSTree.showNodeAsJSONJSTree),
    path('django_jstree/showtree/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>/<int:rootnode>', jsTree.showJSTree),
    path('django_jstree/showtree/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>', jsTree.showJSTree),
    path('django_jstree/showtree/<slug:treename>', jsTreeByName.showJSTreeByName),
    path('django_jstree/showtree/<slug:treename>>/<int:rootnode>', jsTreeByName.showJSTreeByName),
]
