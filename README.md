This project is a simple plugin framework for Python 3.

Authors
=======
It is a fork from [A Simple Plugin Framework][1] by Marty Alchin.

Régis Décamps maintains this project.

Design and Notions
========
* The program is extensible, and extensions are made on *mount points*.
* A specific mount point is defined as a class with ``metaclass=spf.MountPoint``
* An extension comes as independant class that inherit from the appropriate mount point.
* A *plugin* is a package of one or more extensions. It comes as a python package.
* Importing the plugin is enough to active the mount point and glue all code together.
* The class ``MountPoint`` as well as utility functions constitute the framework and are shipped in ``spf.py``
  * utility method ``load_plugins()`` loads all plugins in the ``plugins`` directory
  * utility decorator ``ExtensionsAt(klassMountPoint)`` returns a list of extensions that are loaded for this mount point.

In this sample

* ``program.py`` is a simple program that prints "hello world" with a transformation performed by all plugins
* The mount points for this sample are in ``mount_point.py`` 
  * The mount point ``TextTransformer`` expects a method ``transform_text(string)``
* The plugins are placed in the directory ``plugins`` and loaded with the utility function ``spf.load_plugins()``
  * There is only one plugin called ``html_transformer``that ships three extensions for the mount point ``TextTransformer``

This project also has an [introduction on my blog][2].

[1]: http://martyalchin.com/2008/jan/10/simple-plugin-framework/
[2]: http://regis.decamps.info/blog/2012/05/simple-framework-for-python-plugins/