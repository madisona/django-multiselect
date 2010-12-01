
from setuptools import setup

setup(
    name="django-multiselect",
    version="0.1",
    description="Django Buildout application using multiselect",
    author="Matt Morrison and Aaron Madison",

    package_dir={'': 'src'},
    install_requires = (
        'django',
    ),
)
