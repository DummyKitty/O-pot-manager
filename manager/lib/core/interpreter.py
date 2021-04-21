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
from manager.modules.openresty.Openresty import Openresty
from manager.modules.opot.Opot import Opot


class BaseInterpreter(object):
    def __init__(self):
        self.censys_uid = CENSYS_UID
        self.censys_secret = CENSYS_SECRET
        self.zoomeye_username = ZOOMEYE_USERNAME
        self.zoomeye_password = ZOOMEYE_PASSWORD
        self.prompt_hostname = "manager"
        self.current_module = None
        self.__parse_prompt()

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
                    command_handler(args.split(" "))
            except EOFError:
                break
            except KeyboardInterrupt:
                print("Bye...")
                break

    @property
    def prompt(self):
        if self.current_module:
            try:
                return self.module_prompt_template.format(
                    host=self.prompt_hostname, module=self.module_metadata)
            except (AttributeError, KeyError):
                return self.module_prompt_template.format(
                    host=self.prompt_hostname, module="UnnamedModule")
        else:
            return self.raw_prompt_template.format(host=self.prompt_hostname)

        return "manager> "

    def get_command_handler(self, command):
        try:
            handler = getattr(self, "command_" + command)
        except AttributeError:
            return False
        return handler

    def __parse_prompt(self):
        raw_prompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 > "
        self.raw_prompt_template = raw_prompt_default_template
        module_prompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 (\001\033[91m\002{module}\001\033[0m\002) > "
        self.module_prompt_template = module_prompt_default_template


class Interpreter(BaseInterpreter):
    def __init__(self, base_dir):
        super(Interpreter, self).__init__()
        self.conf_path = base_dir + CONFIF_PATH
        self.banner = BANNER
        self.db_path = base_dir + DATABASE_PATH
        self.knowledgeDb = knowledgeDataBase(self.db_path)

        print(self.banner)

    def command_help(self, *args, **kwargs):
        help_message = """Global commands:
        help                            Print this help menu
        shodan  <service type>          Search for web service domain via shodan
        zoomeye <service type>          Search for web service domain via zoomeye (Recomand)
        censys  <service type>          Search for web service domain via censys
        fofa    <service type>          Search for web service domain via fofa

        show    <services|cves> <num>   
                services                Show the services
                cves                    Show all latest CVE
        delete  <services|cves>         Delete from knowledge database
        
        use     <modules>               Use modules
                openresty               Use openresty module
                opot                    Use opot module
        banner                          Print banner
        exit                            Exit manager"""
        print(help_message)

    # def command_search(self, *args, **kwargs):
    #     pass

    def command_exit(self, *args, **kwargs):
        print("Bye..")
        raise EOFError

    # def command_use(self):

    def command_shodan(self, args):
        search_result = Shodan(conf_path=self.conf_path,
                               token=self.shodan_token)

    def command_banner(self, *args, **kwargs):
        print(self.banner)

    def command_zoomeye(self, args):
        if len(args) > 0:
            args = " ".join(args)
            search_result = ZoomEye(
                conf_path=self.conf_path,
                username=self.zoomeye_username,
                password=self.zoomeye_password).search(args)
            self._insert_into_knowledgeDb("services", search_result)
        else:
            print("please search something")

    def command_fofa(self, args):
        search_result = Fofa(conf_path=self.conf_path,
                             user=self.fofa_email,
                             token=self.fofa_token)

    def command_censys(self, args):  # censys不太好用，返回所有端口，选择不是很方便
        if len(args) > 0:
            args = " ".join(args)
            search_result = Censys(conf_path=self.conf_path,
                                   uid=self.censys_uid,
                                   secret=self.censys_secret).search(args)
            self._insert_into_knowledgeDb("services", search_result)
        else:
            print("please search something")

    def command_show(self, args):
        table_name = args.pop(0)
        if table_name == 'services':
            self._show_services(args)
        elif table_name == 'cves':
            self._show_cves(args)
        elif table_name == None:
            print("show services | show cves")
            self.command_help()
        else:
            print("不支持该命令")
            self.command_help()

    def command_delete(self, table_name):
        table_name = " ".join(table_name)
        if table_name in self.knowledgeDb.white_tables:
            self.knowledgeDb.delete(table_name=table_name, allrange=True)

    def _show_services(self, args):
        service_type = args[0] if len(args) > 0 else None
        limit = args[1] if len(args) > 1 else None
        res = self.knowledgeDb.select("services",
                                      service_name=service_type,
                                      limit=limit)
        tb = PrettyTable(["service_type", "domain", "ip", "port"])
        for i in res:
            tb.add_row(list(i))
        print(tb)

    def _show_cves(self, *args, **kwargs):
        service_type = args[0] if len(args) > 0 else None
        limit = args[1] if len(args) > 1 else None
        res = self.knowledgeDb.select("services",
                                      service_name=service_type,
                                      limit=limit)
        tb = PrettyTable(["service_type", "domain", "ip", "port"])
        for i in res:
            tb.add_row(list(i))
        print(tb)

    def _show_help(self):
        self.command_show_help()

    def _insert_into_knowledgeDb(self, table_name, knowledges):
        if table_name in self.knowledgeDb.white_tables:
            for i in knowledges:
                self.knowledgeDb.insert(table_name, i)
                # table_name, [i.service_type, i.domain, i.ip, i.port])
        else:
            pass

    def command_use(self, module, *args, **kwargs):
        module_path = module[0]
        if module_path == "openresty":
            # module_path = self.base_dir + "modules/openresty"
            self.current_module = Openresty()
        elif module_path == "opot":
            self.current_module = Opot()

    def command_services(self, func):
        if self.current_module:
            if func:
                try:
                    module_handler = self.get_module_func_handler(func)
                    if module_handler:
                        module_handler()
                except:
                    return
        else:
            print("please use a module eg:openresty|opot")

    def command_back(self, *args, **kwargs):
        self.current_module = None

    def get_module_func_handler(self, func):
        try:
            handler = getattr(self.current_module, "service" + func)
        except AttributeError:
            return False
        return handler


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


# def load_file_to_module(module_path):
#     try:

#     except ImportError:
#         print("load module {} failed".format(module_path))
# 动态导入不写了