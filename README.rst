=====
Django_jsTree
=====

Django_jsTree provides a jsTree view of a treebeard tree using Django models and an optional database configuration


Quick start
-----------

1. Install django_jstree using pip like this::
    pip install django_jstree
    
2. Add "django_jstree" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_unmaskpasswordinput',
    ]

3. (optional) Run `python manage.py collectstaticfiles` to copy the required js, css, and resources
to your static files location

4. Run ``python manage.py migrate`` to create the models in your database.

5. Display a tree by either: defining the tree in the administrator or browsing to::
    jstree/showtree/treebeardmodel/leafmodellist/rootnodeid
