"""
    (c) 2018-2019 Sam Caldwell.  All Rights Reserved.
"""
from os import path
from os.path import dirname
from time import time
import setuptools.command.build_py

HERE = path.abspath(dirname(dirname(dirname(__file__))))
SETUP_DIR = "setup"


class BumpVersion(setuptools.command.build_py.build_py):
    """
        Bump the version.txt file.
    """

    @staticmethod
    def bump_version():
        """
            read the VERSION.txt file.  Parse the version number then bump.

            :return:
        """
        src_fn = path.join(HERE, SETUP_DIR, "VERSION.txt")
        c_time = time()
        version = f"{str(c_time)[0:4]}.{str(c_time)[4:7]}.{str(c_time)[7:10]}"

        with open(src_fn, mode='w', encoding='utf-8') as src:
            src.write(version)

    def run(self):
        """
            On build, bump the version.
            :return:
        """
        self.bump_version()
