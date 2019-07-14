"""
    (c) 2018-2019 Sam Caldwell.  See LICENSE.txt
"""
from setuptools import setup, find_packages
from setup.build_tools.read_setup_conf import read_setup_conf
from setup.build_tools.readfile import readfile
from setup.build_tools.bump_version import BumpVersion
from setup.build_tools.clean_artifact import CleanArtifact
from setup.build_tools.initialize_project import InitializeProject

setup(
    name=read_setup_conf("PROJECT_NAME.txt"),
    version=read_setup_conf("VERSION.txt"),
    description=read_setup_conf("DESCRIPTION.txt"),
    long_description=readfile('README.md'),
    url=read_setup_conf("URL.txt"),
    author=read_setup_conf("AUTHOR.txt"),
    author_email=read_setup_conf("AUTHOR_EMAIL.txt"),
    classifiers=read_setup_conf("CLASSIFIERS.txt").split('\n'),
    packages=find_packages(
        exclude=[
            'contrib',
            'docs',
            'tests',
            'setup',
            'build_tools'
        ]
    ),
    python_requires='>=3.7, <4',
    install_requires=readfile("requirements.txt").split('\n'),
    extras_require={
        'dev': readfile("requirements.dev.txt").split('\n'),
        'test': readfile("requirements.test.txt").split('\n'),
    },
    cmdclass={
        'clean_artifact': CleanArtifact,
        'bump_version': BumpVersion,
        'init': InitializeProject,
    },
    entry_points={
        'console_scripts': [
            'myapp=src:main',
        ],
    }
)
