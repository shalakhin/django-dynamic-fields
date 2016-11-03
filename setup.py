from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='dynamic',
      version='0.0.1',
      description="leverage JSONField and PostgreSQL jsonb to provide " + \
                   "full-featured Django db.models functionality",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author="Olexandr Shalakhin",
      author_email='olexandr@shalakhin.com',
      url='https://github.com/shalakhin/dynamic',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      dynamic=dynamic.scripts.cli:cli
      """
      )
