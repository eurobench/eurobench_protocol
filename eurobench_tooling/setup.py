from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='eurobench_tooling',
    description=('Tool for checking a yaml template spec.'),
    long_description=long_description,
    author='Anthony Remazeilles',
    author_email='anthony.remazeilles@tecnalia.com',
    url='https://github.com/',
    license='Apache 2.0',
    packages=['eurobench_tooling'],
    scripts=['script/check_template'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )
