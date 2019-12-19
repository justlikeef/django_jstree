from django.shortcuts import render
import random

def showJSTree(request, appname, treemodelname, leafmodelname, rootnode = 0):
    _imp = __import__(appname+'.models',globals(), locals(), [treemodelname])
    model = getattr(_imp, treemodelname)
    return render(request, "jstree/jsTree.html", {'treename':treemodelname+"_"+str(random.getrandbits(32)), 'appname':appname, 'treemodelname':treemodelname, 'leafmodelname':leafmodelname, 'startnode':rootnode})