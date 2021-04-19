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
from configparser import ConfigParser

from manager.lib.core.data import *
from manager.modules.search_engines.zoomeye import ZoomEye
from manager.modules.search_engines.shodan import Shodan
from manager.modules.search_engines.fofa import Fofa
from manager.modules.search_engines.censys import Censys
from manager.lib.core.log import logger
from manager.thirdparty.prettytable.prettytable import PrettyTable
from manager.lib.core.db import knowledgeDataBase


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
    def __init__(self, module_path):
        super(Interpreter, self).__init__()
        self.config_path = CONFIF_PATH
        self.banner = BANNER
        self.db_path = module_path + DATABASE_PATH
        self.knowledgeDb = knowledgeDataBase(self.db_path)
        print(self.banner)

    def command_help(self, *args, **kwargs):
        help_message = """Global commands:
        help                        Print this help menu
        shodan  <search term>        Search for web service domain
        zoomeye|show all               Show all latest CVE
        show    <services|cves>
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
                                username=self.zoomeye_username,
                                password=self.zoomeye_password)

    def command_fofa(self, *args, **kwargs):
        search_result = Fofa(conf_path=self.conf_path,
                             user=self.fofa_email,
                             token=self.fofa_token)

    def command_censys(self, *args, **kwargs):
        search_result = Censys(conf_path=self.conf_path,
                               uid=self.censys_uid,
                               secret=self.censys_uid)

    def command_show(self, *args, **kwargs):
        table_name = args[0]
        if table_name == 'services':
            service_type = args[1] if args[1] else None

            port = kwargs['port']
            res = self.knowledgeDb.select("services",
                                          service_type=service_type,
                                          ip=ip,
                                          port=port)
            tb = PrettyTable([])
        elif table_name == 'cves':
            pass
        elif table_name == None:
            print("show services | show cves")
            self.command_help()
        else:
            print("不支持该命令")
            self.command_help()

    def _show_services(self, *args, **kwargs):
        self.knowledgeDb.select("")

    def _show_cves(self, *args, **kwargs):
        pass

    def _show_help(self):
        self.command_show_help()


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
    except Exception as ex:
        print(ex)
        return ["未找到该命令"]
    return stdout
