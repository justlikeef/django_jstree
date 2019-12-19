from django.core import serializers
from django.http import HttpResponse
from django_jstree.core.serializers.jsTreeNode import JSTreeNodeSerializer
        
def showNodeAsJSONJSTree(request, appname, treemodelname, leafmodelname=None, nodeid=0):
    _imp = __import__(appname+'.models',globals(), locals(), [treemodelname])
    treemodel = getattr(_imp, treemodelname)
    myserializer = JSTreeNodeSerializer()
    if nodeid == 0:
        return HttpResponse(content=myserializer.serialize(treemodel.get_root_nodes(), max_depth=0, leafmodelname=leafmodelname), content_type="application/json")      
    else:
        return HttpResponse(content=myserializer.serialize(treemodel.objects.filter(id=nodeid), max_depth=0, leafmodelname=leafmodelname), content_type="application/json")