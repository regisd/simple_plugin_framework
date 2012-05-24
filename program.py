#/usr/bin/python
# -*- coding: UTF-8 -*-
import mount_point
import spf

__author__ = 'Régis Décamps'

#load plugins in the ``plugins``directory
all_plugins = spf.load_plugins()

class MyProgram:
    # descriptor can be be invoked automatically only upon attribute access.
    text_plugins = spf.ExtensionsAt(mount_point.TextTransformer)
    def main(self):
        # Here I declare a mount point TextTransformer
        # "hello world" will be printed by each plugin
        for plugin in self.text_plugins:
            retval = plugin.transform_text("hello world")
            print("Plugin {plugin} produces {retval}".format(plugin=plugin, retval=retval))

if __name__ == '__main__':
    prog = MyProgram()
    prog.main()