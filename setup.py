#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
import os


def get_packages(package):
    return [dirpath for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename) for filename in filenames])
    return {package: filepaths}

setup(
    name='django_sms_wrapper',
    version='1.0.1',
    packages=get_packages('sms_wrapper'),
    package_data=get_package_data('sms_wrapper'),
    long_description='test',
    install_requires=['requests>=2.7.0'],
    url='https://github.com/vir-mir/sms_wrapper',
    license='MIT',
    author='vir-mir',
    keywords='django sms wrapper',
    author_email='virmir49@gmail.com',
    description='wrapper django sms framework',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
