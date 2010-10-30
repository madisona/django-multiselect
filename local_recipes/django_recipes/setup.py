
from setuptools import setup

setup(name="django_recipes",
      entry_points = """
      [zc.buildout]
      wsgi = script:Wsgi
      django = script:Django
      """)
