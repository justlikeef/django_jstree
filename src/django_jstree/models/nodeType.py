from django.db import models
from django_jstree.models import jstree


class nodeType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(default='', blank=True)
    jsTree = models.ForeignKey( "jstree", on_delete=models.CASCADE,
                                verbose_name="Trees",
                                help_text="Apply this type to these trees.")
    maxChildren = models.IntegerField(default=-1,
                                      verbose_name="Maximum number of child nodes for this type (-1 unlimited)")
    maxDepth = models.IntegerField( default=-1,
                                    verbose_name="Maximum depth of children for this node type (-1 unlimited)")
    iconClass = models.CharField(   default='', blank=True,
                                    max_length=30,
                                    verbose_name="CSS class",
                                    help_text="CSS class name to add to nodes of this type")
    liAttributes = models.TextField(default='', blank=True,
                                    verbose_name="LI Attributes",
                                    help_text="Additional attributes to add to the generated LI element")
    aAttributes = models.TextField(default='', blank=True,
                                    verbose_name="A Attributes",
                                    help_text="Additional attributes to add to the generated A element")
    childNodeTypes = models.ManyToManyField("nodeType",
                                            verbose_name="Valid Child Node Types",
                                            help_text="Restricts the type of children this node can have (leave empty for no restrictions)")
    
    def __str__(self):
        return self.name
