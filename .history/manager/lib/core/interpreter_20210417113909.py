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

from manager.lib.core.data import *
from manager.modules.zoomeye import ZoomEye
from manager.modules.shodan import Shodan
from manager.modules.fofa import Fofa
from manager.lib.core.log import logger


class BaseInterpreter(object):
    def __init__(self):
        pass

    def start(self):
        while True:
            try:
                command = input(self.prompt)
                command, _, args = command.strip().partition(" ")
                command_handler = self.get_command_handler(command)
                if command_handler == False:
                    for i in cmd_exec(command, args):
                        print(i)
                else:
                    command_handler(args)
            except EOFError:
                break

    @property
    def prompt(self):
        return "manager> "

    def get_command_handler(self, command):
        try:
            handler = getattr(self, "command_" + command)
        except AttributeError:
            return False
        return handler


class Interpreter(BaseInterpreter):
    def __init__(self):
        super(Interpreter, self).__init__()
        self.config_path = CONFIF_PATH
        self.banner = BANNER

        print(self.banner)

    def command_help(self, *args, **kwargs):
        help_message = """Global commands:
        help                        Print this help menu
        search <search term>        Search for web service domain
        list|show all               Show all latest CVE
        exit                        Exit manager"""
        print(help_message)

    def command_search(self, *args, **kwargs):
        pass

    def command_exit(self, *args, **kwargs):
        print("Bye..")
        raise EOFError

    # def command_use(self):

    def command_shodan(self, *args, **kwargs):
        search_result = Shodan(conf_path=self.conf_path,
                               token=self.shodan_token)

    def command_zoomeye(self, *args, **kwargs):
        search_result = ZoomEye(conf_path=self.conf_path,
                                username=zoomeye_username,
                                password=zoomeye_password)

    def command_fofa(self, *args, **kwargs):
        search_result = Fofa(conf_path=self.conf_path, )


def cmd_exec(command, args):
    cmd = shlex.split(command + " " + args)
    stdout = b''
    try:
        sp = subprocess.Popen(cmd,
                              shell=False,
                              stderr=subprocess.PIPE,
                              stdout=subprocess.PIPE)
        stdout, stderr = sp.communicate()
        encoding = chardet.detect(stdout).get("encoding")
        encoding = encoding if encoding else "utf-8"
        stdout = stdout.split(b'\n')
        for i, data in enumerate(stdout):
            stdout[i] = data.decode(encoding, errors='ignore')
        # output = b""
        # while sp.poll() is None:
        #     line = sp.stdout.read()
        #     output += line
    except:
        return ["未找到该命令"]
    return stdout
