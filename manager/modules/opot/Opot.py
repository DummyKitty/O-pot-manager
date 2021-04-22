#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :Opot.py
@Description :
@Date        :2021/04/22 08:43:21
@Author      :dr34d
@Version     :1.0
'''

import os
from manager.lib.core.data import *

class Opot():
    def service_stop(self, *args, **kwargs):
        sure = input(f"{red}Are you sure to stop O-pot?[y|n]{end}")
        if sure == "y" or sure == "Y":
            cmd = "docker-compose -f /opt/tpot/etc/tpot.yml stop"
            try:
                os.system(cmd)
            except Exception as ex:
                print(ex)
        else:
            return

            

    def service_start(self, *args, **kwargs):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yml start"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)
        print(f"{yellow}Please waite for a moment~ {red}Using service status to check{end}")

    def service_restart(self, *args, **kwargs):
        sure = input(f"{red}Are you sure to stop O-pot?[y|n]{end}")
        if sure == "y" or sure == "Y":
            cmd = "docker-compose -f /opt/tpot/etc/tpot.yml restart"
            try:
                os.system(cmd)
            except Exception as ex:
                print(ex)
        else:
            return

    def service_status(self, *args, **kwargs):
        try:
            os.system("bash /opt/tpot/bin/dps.sh")
        except:
            return

    def service_install(self, *args, **kwargs):
        os.system("git clone https://github.com/GreyDr34d/O-Pot.git /root/O-Pot")
        os.system("bash O-Pot/iso/installer/install.sh --type=user")

    def service_unistall(self, *args, **kwargs):
        sure = input(f"{red}Are you sure to uninstall O-pot?[y|n]{end}")
        if sure == "y" or sure == "Y":
            self._delete()

    def service_up(self, *args, **kwargs):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yml up -d"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_down(self, *args, **kwargs):
        sure = input(f"{red}Are you sure to remove O-pot containers?[y|n]{end}")
        if sure == "y" or sure == "Y":
            cmd = "docker-compose -f /opt/tpot/etc/tpot.yml down"
            try:
                os.system(cmd)
            except Exception as ex:
                print(ex)
        else:
            return

    def _delete(self):
        self.service_down()
        os.system("rm -rf /data /opt/tpot")

    def __str__(self):
        return "opot_module"

    def __add__(self, x):
        return "opot_module" + x
