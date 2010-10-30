
import os
import zc

class AbstractScript(object):
    file_name = ""
    template = ""

    def __init__(self, buildout, name, options):
        self.egg = zc.recipe.egg.Egg(buildout, 'django_recipes', options)

        self.executable = buildout['python']['executable']
        self.buildout, self.name, self.options = buildout, name, options

        self.extra_paths = []
        if 'extra-paths' in options:
            self.extra_paths = [path for path in options['extra-paths'].split(' ')]

    def install(self):
        requirements, ws = self.egg.working_set()
        #ws = self.ws
        #self.ws = zc.buildout.easy_install.working_set(
        #    [buildout['python']['eggs']], self.executable,
        #    [buildout['python']['develop-eggs-directory'],
        #    buildout['python']['eggs-directory']])

        script_paths = []
        script_paths.extend(self.create_script(self.extra_paths, ws))
        return script_paths

    def update(self):
        pass

    def create_script(self, extra_paths, ws):
        # save off the default script template, we'll put it back when done
        _script_template = zc.buildout.easy_install.script_template
        
        zc.buildout.easy_install.script_template = \
            zc.buildout.easy_install.script_header + self.template
        script = zc.buildout.easy_install.scripts(
                [(self.file_name, '', '')],
                ws,
                self.executable,
                self.buildout['python']['bin-directory'],
                extra_paths=extra_paths,
                arguments="")
        # put template back
        zc.buildout.easy_install.script_template = _script_template
        return script

class Wsgi(AbstractScript):
    file_name = 'django.wsgi'
    template = """

import os
import sys

sys.path[0:0] = [
    %(path)s,
]

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()

"""

class Django(AbstractScript):
    file_name = "manage.py"
    template = """
import os
import sys

sys.path[0:0] = [
    %(path)s,
]

import manage

if __name__ == '__main__':
    manage.main()
"""
