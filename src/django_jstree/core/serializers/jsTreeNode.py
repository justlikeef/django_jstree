from django.core.serializers.json import Serializer
from django.conf import settings

class JSTreeNodeSerializer(Serializer):
    def _init_options(self):
        self.max_depth = self.options.pop('max_depth', 0)
        self.leaffieldname = self.options.pop('leaffieldname', 0)
        self.applytypes = self.options.pop('applytypes', False)
        if self.leaffieldname.find(','):
          self.leaffieldname = self.leaffieldname.split(',')
        else:
          self.leaffieldname = [self.leaffieldname]
        super()._init_options()

    def get_dump_object(self, obj, curdepth = 0):
        data = {'id': str(obj.path)+'_'+str(obj.id), 'text':str(obj), 'children': [], 'icon':'jstree-root' if curdepth == 0 else 'jstree-branch'}
        if self.applytypes == True:
            data["type"] = "Testing123"
        
        if curdepth <= self.max_depth:
            if obj.get_children_count() > 0:
                for child in obj.get_children():
                    data['children'].append(self.get_dump_object(child, curdepth+1))
            else:
                data['children'] = False
        else:
            data['children'] = True if obj.get_children_count() > 0 else False
               
        for curleaffield in self.leaffieldname:
          if eval('obj.'+curleaffield+'.count()') > 0:
              if isinstance(data['children'], bool):
                  data['children'] = []
                  
              for curleafobj in eval('obj.'+curleaffield+'.all()'):
                  data['children'].append({'id':str(obj.path)+'_'+str(obj.id)+'_'+curleaffield+"_"+str(curleafobj.id), 'text':str(curleafobj), 'icon':'jstree-leaf jstree-' + curleaffield+'-leaf', 'children':False})
        if data['children'] == False: data.pop('children')
        return data