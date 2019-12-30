from django.shortcuts import render
from django_jstree.models.jstree import jstree
from django_jstree.models.nodeType import nodeType
import random

def showJSTreeByName(request, treename, rootnode = 0):
    try:
      jstobj = jstree.objects.get(name__exact=treename)
    except jstree.DoesNotExist:
      print("The requested {} tree does not exist", treename)

    
    _imp = __import__(jstobj.appname+'.models',globals(), locals(), jstobj.treemodelname)
    model = getattr(_imp, jstobj.treemodelname)
    
    typedef = {}
    if jstobj.applyTypes == True:
        # Get the node types for this tree
        for curNodeType in nodeType.objects.filter(jstrees__id=jstobj.id):
            # Build list of valid child nodes
            typedef[curNodeType.name] = { "max_children":curNodeType.maxChildren,
                                        "max_depth":curNodeType.maxDepth,
                                        "valid_children":"",
                                        "icon":curNodeType.iconClass,
                                        "li_attr":curNodeType.liAttributes,
                                        "a_attr":curNodeType.aAttributes
                                      }
            for curChildType in curNodeType.childNodeTypes.all():
                typedef[curNodeType.name]["valid_children"] += curChildType.name + ","

            if len(typedef[curNodeType.name]["valid_children"]) > 0:
                typedef[curNodeType.name]["valid_children"] = typedef[curNodeType.name]["valid_children"][:-1]          
    
    context = { 'treename':treename,
                'appname':jstobj.appname,
                'treemodelname':jstobj.treemodelname,
                'leaffieldname':jstobj.leaffieldname,
                'startnode':rootnode,
                'typeDefs':typedef,
                'enableCheckbox':jstobj.enableCheckbox,
                'enableContextmenu':jstobj.enableContextmenu,
                'enableSearch':jstobj.enableSearch,
                'enableFuzzySearch':jstobj.enableFuzzySearch,
                'showOnlyMatches':jstobj.showOnlyMatches,
                'showOnlyMatchesChildren':jstobj.showOnlyMatchesChildren,
                'enableDND':jstobj.enableDND,
                'enableSort':jstobj.enableSort,
                'enableState':jstobj.enableState,
                'applyTypes':jstobj.applyTypes,
                'enableUnique':jstobj.enableUnique,
                'enableWholerow':jstobj.enableWholerow,
                'enableChanged':jstobj.enableChanged,
                'additionalJS':jstobj.additionalJS
              }
    return render(request, "jstree/jsTree.html", context)