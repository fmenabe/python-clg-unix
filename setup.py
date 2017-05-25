# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='clg-unix',
    version='1.0.0',
    author='François Ménabé',
    author_email='francois.menabe@gmail.com',
    url = 'http://clg.readthedocs.org/en/latest',
    download_url = 'http://github.com/fmenabe/python-clg-unix',
    license='MIT License',
    description='python-unix plugin for clg',
    long_description=open('README.rst').read(),
    keywords=['command-line', 'argparse', 'wrapper', 'clg', 'unix'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
    ],
    py_modules=['clg/unix'],
    install_requires=['unix'])
