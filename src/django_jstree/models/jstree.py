from django.db import models

class jstree(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(default='', blank=True)
    appname = models.CharField(max_length=255)
    treemodelname = models.CharField(max_length=255)
    leaffieldname = models.TextField( default='', 
                                      blank=True,
                                      verbose_name="Leaf fields", 
                                      help_text="Name of one or more fields defined in the model which represent a leaf relationship, seperated by commas. ex. leaf1field[,leaf2field,leafthreefield]")
    enableCheckbox = models.BooleanField( default=False,
                                          verbose_name="Add checkboxes before node?")
    enableContextmenu = models.BooleanField(default=False,
                                            verbose_name="Enable Context Menu Popup?",
                                            help_text="Enabling this option requires you to define the context menu based on the node type.")
    enableSearch = models.BooleanField( default=False,
                                        verbose_name="Enable search?")
    enableFuzzySearch = models.BooleanField(default=False, 
                                            verbose_name="Turn on fuzzy (non-exact) searching and highlighting using simple pattern matching")
    showOnlyMatches = models.BooleanField( default=False,
                                        verbose_name="Only show matches when searching?")
    showOnlyMatchesChildren = models.BooleanField( default=False,
                                        verbose_name="Show the children of matches when searching?")
    enableDND = models.BooleanField(default=False,
                                    verbose_name="Enable drag and drop functionality", help_text="Enabling this option requires additional Javascript to make it do anything")
    enableSort = models.BooleanField(default=False,
                                      verbose_name="Sort Nodes?", help_text="Automaticly sort sibling nodes in alphabetical order.")
    enableState = models.BooleanField(default=False,
                                      verbose_name="Remember Node State?", help_text="Remember if the nodes' state the last time this tree was used.")
    applyTypes = models.BooleanField( default=False,
                                      verbose_name="Add node type?",
                                      help_text="If checked, the method 'getJSTreeType()' will be called on each node in the tree and added to the type parameter on each node. If the function does not exist on the model, then the name of the model class is added to type parameter")
    enableUnique = models.BooleanField( default=False,
                                        verbose_name="Require unique names of sibling nodes?")
    enableWholerow = models.BooleanField( default=False,
                                          verbose_name="Allow click on and highlight whole row when selecting nodes?", help_text="May cause slowness for large trees or on older browsers.")
    enableChanged = models.BooleanField( default=False,
                                          verbose_name="Add additonal change info?", help_text="This plugin adds additional information about selection changes.")
    additionalJS = models.TextField(default='', blank=True)
    
    def __str__(self):
        return self.name
