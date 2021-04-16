#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :interpreter.py
@Description :
@Date        :2021/04/16 11:29:44
@Author      :dr34d
@Version     :1.0
'''

import sys
import chardet
import shlex
import os
import subprocess

from manager.lib.core.data import BANNER


class BaseInterpreter(object):
    def init(self):
        pass

    def start(self):
        while True:
            command = input(self.prompt)
            command, _, args = command.strip().partition()
            command_handler = self.get_command_handler(command)
            if command_handler == False:
                cmd_exec(command, args)
            command_handler()

    @property
    def prompt(self):
        return "manager>"

    def get_command_handler(self, command):
        try:
            handler = getattr(self, "command_" + command)
        except AttributeError:
            return False
        return handler

    def cmd_exec(self, command, args):
        sp = subprocess.Popen(command, args)
        output = sp.stdout.read()
        return output


class Interpreter(BaseInterpreter):
    def init(self):
        super(Interpreter, self).__init__()
        sys.stdout(BANNER)

    def command_help(self):
        pass

    def command_list(self, *args, **kwargs):
        pass

    # def command_use(self):
