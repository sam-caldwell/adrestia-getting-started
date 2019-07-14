"""
    (c) 2018-2019 Sam Caldwell.  All Rights Reserved.
"""
import sys
import glob
import shutil
from os import path
from os.path import dirname, exists
import setuptools.command.build_py

HERE = path.abspath(dirname(dirname(dirname(__file__))))


class CleanArtifact(setuptools.command.build_py.build_py):
    """
        Clean artifacts (*.egg-info and build/)
    """

    def run(self):
        """
            On build, bump the version.
            :return:
        """
        try:
            if exists(path.join(HERE, 'build')):
                shutil.rmtree(path.join(HERE, 'build'))
            eggs = glob.glob("*.egg-info", recursive=True)
            for tgt in eggs:
                if exists(path.join(HERE, tgt)):
                    shutil.rmtree(path.join(HERE, tgt))
        except OSError as error:
            print(f"Error cleaning up artifacts.  Exception: {error}")
            sys.exit(1)
