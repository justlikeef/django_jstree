from django.core.serializers.json import Serializer

class JSTreeNodeSerializer(Serializer):
    def _init_options(self):
        self.max_depth = self.options.pop('max_depth', 0)
        self.leafmodelname = self.options.pop('leafmodelname', 0)
        if self.leafmodelname.find(','):
          self.leafmodelname = self.leafmodelname.split(',')
        else:
          self.leafmodelname = [self.leafmodelname]
        super()._init_options()

    def get_dump_object(self, obj, curdepth = 0):
        data = {'id': obj.id, 'text':str(obj), 'icon':'/static/images/folder.png', 'children': []}
        try:
            curdepth += 1
        except NameError:
            curdepth = 0
        
        if curdepth <= self.max_depth:
            if obj.get_children_count() > 0:
                for child in obj.get_children():
                    data['children'].append(self.get_dump_object(child, curdepth))
            else:
                data['children'] = False
        else:
            data['children'] = True if obj.get_children_count() > 0  else False
        """        
        for curleafmodel in self.leafmodelname:
          if eval('obj.'+curleafmodel+'.count()') > 0:
              if isinstance(data['children'], bool):
                  data['children'] = []
                  
              for curleafobj in eval('obj.'+curleafmodel+'.all()'):
                  data['children'].append({'id':curleafobj.id, 'text':str(curleafobj), 'icon':'/static/images/leaf.png', 'children':False})
        """
        if data['children'] == False: data.pop('children')
        return data