# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import versioneer
import re

LIB_PATTERN = re.compile('^\s*([\w\-\[\]]+)\s*')

with open('./requirements.txt', 'r') as fp:
    requirements = [r.strip() for r in fp]

prod_requires = [r for r in requirements if r and not r.startswith('#')]
dev_requires = [LIB_PATTERN.match(r).group(0) for r in prod_requires]
scripts_require = [
    'redis',
    'pymongo',
    'tqdm',
    'retrying',
    'simplejson',
    'python-slugify',
    'bson',
]

setup(
    name='dailyornate',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Autobloger Service',

    # The project's main homepage.
    url='https://github.com/are-prabhu/dailyornate',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],
    tests_require = [
        'pytest',
        'pytest-mock',
        'pytest-pythonpath',
        'pytest-flask'
    ],
    extras_require = {'dev': dev_requires, 'prod': prod_requires, 'scripts': scripts_require},
    package_dir = {'dailyornate.templates': 'dailyornate/templates'},
    package_data = {'dailyornate.templates': ['*.yaml'], 'dailyornate.udfs': ['*.lua']},
    packages = find_packages(include=['dailyornate', 'dailyornate.*'])
)
