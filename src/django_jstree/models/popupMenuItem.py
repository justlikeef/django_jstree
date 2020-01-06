from django.db import models
from django_jstree.models import nodeType
from django_jstree.models import nodeTypePopupMenuItem
from treebeard.mp_tree import MP_Node

class popupMenuItem(MP_Node):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(default='', blank=True)
    nodeTypes = models.ManyToManyField( "nodeType", 
                                        related_name="popupMenuItems",
                                        blank=True, 
                                        through="nodeTypepopupMenuItem", 
                                        verbose_name="Apply to Node Types:",
                                        help_text="This popup menu item will apply to this node type")
    menuLabel = models.CharField(default='', 
                                blank=True,
                                max_length=255,
                                verbose_name="Menu Text",
                                help_text="Text to show on popup menu")
    menuTooltip = models.CharField(default='', 
                                blank=True,
                                max_length=255,
                                verbose_name="Tooltip",
                                help_text="Help text to show for menu item")
    seperatorBefore = models.BooleanField(  default=False,
                                            verbose_name="Seperator Before?",
                                            help_text="Show a seperator before this menu item")
    seperatorAfter = models.BooleanField(   default=False,
                                            verbose_name="Seperator After?",
                                            help_text="Show a seperator after this menu item")
    menuItemClass = models.CharField(   default='', 
                                        blank=True,
                                        max_length=255,
                                        verbose_name="Menu Text Class",
                                        help_text="CSS Class to apply to menu text")
    menuClickJSFunction = models.CharField( default='', 
                                            blank=True,
                                            max_length=255,
                                            verbose_name="Call on click",
                                            help_text="Name of Javascript function to call on click")
    shortcut = models.SmallIntegerField(default=0,
                                        verbose_name="Shortcut Keycode",
                                        help_text="KeyCode which will trigger the action if the menu is open (for example 113 for rename, which equals F2)")
    shortcutLabel = models.CharField(   default='', 
                                        blank=True,
                                        max_length=20,
                                        verbose_name="Shortcut Label",
                                        help_text="Shortcut label (like for example F2 for rename)")
    childMenuItems = models.ManyToManyField("popupMenuItem",
                                            related_name="parentMenuItems",
                                            verbose_name="Child Menu Items", 
                                            blank=True)

    def __str__(self):
        return self.name
