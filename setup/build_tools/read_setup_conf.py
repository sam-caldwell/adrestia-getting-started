"""
    (c) 2018-2019 Sam Caldwell.  All Rights Reserved.
"""
from os import path
from os.path import dirname

HERE = path.abspath(dirname(dirname(dirname(__file__))))
SETUP_DIR = "setup"


def read_setup_conf(file_name: str) -> str:
    """

    :param file_name:
    :return:
    """
    with open(path.join(HERE, SETUP_DIR, file_name), mode='r',
              encoding='utf-8') as src:
        return src.read()
