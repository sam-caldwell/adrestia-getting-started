"""
    (c) 2018-2019 Sam Caldwell.  All Rights Reserved.
"""
from os import path
from os.path import dirname

HERE = path.abspath(dirname(dirname(dirname(__file__))))


def readfile(file_name: str) -> str:
    """

    :param file_name:
    :return:
    """
    with open(path.join(HERE, file_name), mode='r', encoding='utf-8') as src:
        return src.read()
