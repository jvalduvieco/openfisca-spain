#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Barcelona',
    version='1.0.0',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description=u'OpenFisca tax and benefit system for Barcelona',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/openfisca-barcelona',
    entry_points = {
        'console_scripts': ['openfisca-debug-test=openfisca_barcelona.scripts.debug_test:main'],
    },
    include_package_data=True,  # Will read MANIFEST.in
    install_requires=[
        'gunicorn >=20.0.0,<21.0.0',
        'Werkzeug >=1.0.0, <2.0.0',
        'OpenFisca-Core[web-api] >=34.0, <35.0',
    ],
    extras_require={
        'test': [
            'flake8',
            'flake8-print',
            'nose',
            'pydevd',
        ]
    },
    packages=find_packages(),
    test_suite='nose.collector',
    )
