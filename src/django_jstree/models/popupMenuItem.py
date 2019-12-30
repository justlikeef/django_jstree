from django.db import models
from django_jstree.models import nodeType


class popupMenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(default='', blank=True)
    nodeTypes = models.ManyToManyField("nodeType", blank=True, through="nodeTypepopupMenuItem", 
                                            verbose_name="Apply to Node Types:",
                                            help_text="This popup menu item will apply to this node type")
    menuText = models.CharField(   default='', blank=True,
                                    max_length=255,
                                    verbose_name="Menu Text",
                                    help_text="Text to show on popup menu")
    menuTextClass = models.CharField(   default='', blank=True,
                                    max_length=255,
                                    verbose_name="Menu Text Class",
                                    help_text="CSS Class to apply to menu text")
    menuClickJSFunction = models.CharField(   default='', blank=True,
                                    max_length=255,
                                    verbose_name="Call on click",
                                    help_text="Name of Javascript function to call on click")

    def __str__(self):
        return self.name

class nodeTypePopupMenuItem(models.Model):
    nodeType = models.ForeignKey("nodeType", on_delete=models.CASCADE)
    popupMenuItem = models.ForeignKey("popupMenuItem", on_delete=models.CASCADE)
    displayOrder = models.IntegerField( default=0,
                                        verbose_name="Display order",
                                        help_text="Order to display in on popup Menu"
                                      )
    
    class Meta:
        ordering = ["displayOrder"]