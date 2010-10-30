
from setuptools import setup

setup(
    name="django-project",
    version="0.1",
    description="Django app using buildout",
    author="Aaron Madison",

    package_dir={'': 'src'},
    install_requires = (
        'django==1.2.3',
        'mock',          # used for testing purposes
        'pyyaml',        # useful for fixtures and testing

#        'south',         # incredibly useful for database migrations
#        'coverage',      # useful for continuous integration, tells how much of code is covered by tests 
#        'clonedigger',   # useful for continuous integration, looks for duplicate chunks of code
#        'unittest-xml-reporting', # useful for continuous integration, makes nice test results
#        'pylint',        # useful for continuous integration, looks at code quality
    ),
)
