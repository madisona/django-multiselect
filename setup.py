
from setuptools import setup

setup(
    name="django-multiselect",
    version="0.1",
    description="Django Buildout application using multiselect",
    author="Matt Morrison and Aaron Madison",
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    packages=('multiselect',),
    package_dir={'': 'src'},
    install_requires = (
        'django',
#        'south',
    ),
)
