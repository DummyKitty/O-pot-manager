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
                    if command:
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
                    host=self.prompt_hostname, module=self.current_module)
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
    help_message = f"""{yellow}Global commands:{red}
    help{end}                             Print this help menu{red}
    shodan{end}   <service type>          Search for web service domain via shodan{red}
    zoomeye{end}  <service type>          Search for web service domain via zoomeye (Recomand){red}
    censys{end}   <service type>          Search for web service domain via censys{red}
    fofa{end}     <service type>          Search for web service domain via fofa{red}

    show{end}     <services|cves> <num>   
             services                Show the services
             cves                    Show all latest CVE{red}
    delete{end}   <services|cves>         Delete from knowledge database{red}
    
    use{end}      <modules>               Use modules
             openresty               Use openresty module
             opot                    Use opot module{red}
    banner{end}                           Print banner{red}
    exit{end}                             Exit manager{end}
    """

    openresty_module_help_message = f"""{yellow}openresty_module command{red}
    help{end}                                 Print this help menu.{red}
    service{end}  <operation> 
             reload                      Reload openresty.
             stop                        Stop openresty.
             start                       Start openresty.
             restart                     Restart openresty.
             add    <service id>         Add services into prepared services table with id.
                                         (using: "show services" to view the id)
                                         (eg: service add 1 2 5 23)
             list                        List prepared services to be deployed.
             clear                       Clear prepared services table.
             current                     List running services.
             update <proxy_services>     Update openresty reverse proxies using prepared
                                         services.{end}
    """
    opot_module_help_message = f"""{yellow}opot_module command{red}
    help{end}                                Print this help menu.{red}
    service{end} <operation> 
            stop                        Stop opot.
            start                       Start opot.
            restart                     Restart opot.
            status                      Show the opot status.
            up                          Up the opot in daemon.
            down                        Down the opot.
            install                     Install the opot.
            unistall                    Unistall the opot.
    """

    def __init__(self, base_dir):
        super(Interpreter, self).__init__()
        self.conf_path = base_dir + CONFIF_PATH
        self.banner = BANNER
        self.knowledgeDb = knowledgeDataBase()
        print(self.banner)

    def command_help(self, *args, **kwargs):
        if self.current_module:
            self.get_module_help()
        else:
            print(self.help_message)

    def get_module_help(self):
        print(self.help_message)
        if self.current_module:
            print(getattr(self, self.current_module + "_help_message"))

    def command_exit(self, *args, **kwargs):
        print("Bye..")
        raise EOFError

    def command_banner(self, *args, **kwargs):
        print(self.banner)


    def command_shodan(self, args):
        search_result = Shodan(conf_path=self.conf_path,
                               token=self.shodan_token)
        print("Not yet developed")
        return

    def command_zoomeye(self, args):
        if len(args) > 0:
            args = " ".join(args)
            search_result = ZoomEye(
                conf_path=self.conf_path,
                username=self.zoomeye_username,
                password=self.zoomeye_password).search(args)
            self._insert_into_knowledgeDb("services", search_result)
            self.command_show(["services"])
        else:
            print("please search something")

    def command_fofa(self, args):
        search_result = Fofa(conf_path=self.conf_path,
                             user=self.fofa_email,
                             token=self.fofa_token)
        print("Not yet developed")

    def command_censys(self, args):  # censys不太好用，返回所有端口，选择不是很方便
        print("Not yet developed")
        return

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
        else:
            print("Table name not exist. Please use 'services'.")

    def _show_services(self, args):
        service_type = args[0] if len(args) > 0 else None
        limit = args[1] if len(args) > 1 else None
        res = self.knowledgeDb.select("services",
                                      service_name=service_type,
                                      limit=limit)
        tb = PrettyTable(["id", "service_type", "domain", "ip", "port"])
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
        self.command_help()

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
            self.current_module = Openresty()
        elif module_path == "opot":
            self.current_module = Opot()
        else:
            print("module not found. Use: help")

    def command_service(self, params):
        func = params.pop(0)
        args = " ".join(params)
        if self.current_module:
            if func:
                try:
                    module_handler = self.get_module_func_handler(func)
                    if module_handler:
                        module_handler(args)
                    else:
                        self.get_module_help()
                except Exception as ex:
                    print(ex)
                    return
            else:
                print("Please add operation")
                print(getattr(self, self.current_module + "_help_message"))

        else:
            print("please use a module eg:openresty|opot")

    def command_back(self, *args, **kwargs):
        try:
            self.current_module.prepare_services = []
        except:
            pass
        self.current_module = None

    def get_module_func_handler(self, func):
        try:
            handler = getattr(self.current_module, "service_" + func)
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