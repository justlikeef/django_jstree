from django.contrib import admin
from django.urls import path
from django_jstree.views import jsTree
from django_jstree.views import jsTreeByName
from django_jstree.views import NodeAsJSONJSTree

urlpatterns = [
    path('shownode/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>/<int:nodeid>', NodeAsJSONJSTree.showNodeAsJSONJSTree),
    path('showtree/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>/<int:rootnode>', jsTree.showJSTree),
    path('showtree/<slug:appname>/<slug:treemodelname>/<slug:leaffieldname>', jsTree.showJSTree),
    path('showtree/<slug:treename>', jsTreeByName.showJSTreeByName),
    path('showtree/<slug:treename>>/<int:rootnode>', jsTreeByName.showJSTreeByName),
]
