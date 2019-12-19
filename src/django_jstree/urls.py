from django.contrib import admin
from django.urls import path
from django_jstree.views import jsTree
from django_jstree.views import NodeAsJSONJSTree

urlpatterns = [
    path('shownode/<slug:appname>/<slug:treemodelname>/<slug:leafmodelname>/<int:nodeid>', NodeAsJSONJSTree.showNodeAsJSONJSTree),
    path('showtree/<slug:appname>/<slug:treemodelname>/<slug:leafmodelname>/<int:rootnode>', jsTree.showJSTree),
    path('showtree/<slug:appname>/<slug:treemodelname>/<slug:leafmodelname>/', jsTree.showJSTree),
    path('showtree/<slug:appname>/<slug:treemodelname>/<slug:leafmodelname>', jsTree.showJSTree),
]
