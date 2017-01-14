from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='activityio',
    version='0.0.3',
    description='Exercise data handling library',
    long_description=long_description,
    url='https://github.com/jmackie4/activityio',
    author='Jordan Mackie',
    author_email='jmackie@protonmail.com',
    license='MIT',
    keywords='exercise cycling running garmin data',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=('references', 'scripts')),

    install_requires=[
        'numpy>=1.11.1',
        'pandas>=0.18.1',
        # copy+pasted from pandas setup.py
        'python-dateutil >= 2',
        'pytz >= 2011k',
    ],
    extras_require={
        'dev': ['xlrd>=1.0.0'],
        'test': [],
    },
    entry_points={
        'console_scripts': [
            'aio=activityio._util.cli:parse',
        ],
    },
)
