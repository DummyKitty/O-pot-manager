#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :main.py
@Description :
@Date        :2021/04/16 11:28:01
@Author      :dr34d
@Version     :1.0
'''

import sys
import os

try:
    import opot_manager
except ImportError:
    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from manager.lib.core.interpreter import Interpreter


def module_path():
    """
    This will get us the program's directory
    """
    return os.path.dirname(os.path.realpath(__file__))


def check_env():
    pass


def init_option():
    pass


def main():
    check_env()
    init_option()
    s = Interpreter()
    s.start()


if __name__ == '__main__':
    main()