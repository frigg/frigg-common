# -*- encoding: utf8 -*-
from setuptools import setup, find_packages

setup(
    name='frigg-common',
    version='0.1.1',
    description='Utils for frigg apps',
    author='The frigg team',
    author_email='hi@frigg.io',
    license='MIT',
    url='https://github.com/frigg/frigg-common',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'frigg-coverage',
        'pyyaml',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python',
    ]
)
