from django.db import models
from django_jstree.models import nodeType
from django_jstree.models import popupMenuItem

class nodeTypePopupMenuItem(models.Model):
    nodeType = models.ForeignKey(   "nodeType", 
                                    on_delete=models.CASCADE)
    popupMenuItem = models.ForeignKey(  "popupMenuItem", 
                                        on_delete=models.CASCADE)
    displayOrder = models.IntegerField( default=0,
                                        verbose_name="Display order",
                                        help_text="Order to display in on popup Menu"
                                      )

    class Meta:
        ordering = ["displayOrder"]