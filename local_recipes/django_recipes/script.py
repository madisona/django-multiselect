
import os
import zc

class AbstractScript(object):
    file_name = ""
    template = ""

    def __init__(self, buildout, name, options):
        self.extra_paths = []
        if buildout['buildout'].get('extra-paths'):
            self.extra_paths = [path 
                for path in buildout['buildout'].get('extra-paths', '').split(' ')]

        self.executable = buildout['python']['executable']
        self.name = name
        self.buildout = buildout
        self.options = options

        self.ws = zc.buildout.easy_install.working_set(
            [buildout['python']['eggs']], self.executable,
            [buildout['python']['develop-eggs-directory'],
            buildout['python']['eggs-directory']])

    def install(self):
        script_paths = []
        script_paths.extend(self.make_scripts(self.extra_paths))
        return script_paths

    def update(self):
        pass

    def make_scripts(self, extra_paths):
        scripts = []
        _script_template = zc.buildout.easy_install.script_template
        zc.buildout.easy_install.script_template = \
            zc.buildout.easy_install.script_header + self.template
        scripts.extend(
            zc.buildout.easy_install.scripts(
                [(self.file_name, '', '')],
                self.ws,
                self.executable,
                self.buildout['python']['bin-directory'],
                extra_paths=extra_paths,
                arguments=""))
        zc.buildout.easy_install.script_template = _script_template
        return scripts

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
