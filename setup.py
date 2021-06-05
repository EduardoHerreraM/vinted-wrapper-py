import pathlib
from setuptools import find_packages, setup

import versioneer

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='stockx-wrapper-py',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Simple Vinted Api for python 3',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/EduardoHerreraM/vinted-wrapper-py',
    author='EduardoHerreraM',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'requests'
    ]
)