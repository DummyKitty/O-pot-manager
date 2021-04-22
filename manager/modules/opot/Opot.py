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


class Opot():
    def service_stop(self, *args, **kwargs):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml stop"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_start(self, *args, **kwargs):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml start"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_restart(self, *args, **kwargs):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml restart"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_status(self, *args, **kwargs):
        try:
            os.system("bash /opt/tpot/bin/dps.sh")
        except:
            return

    def service_install(self, *args, **kwargs):
        os.system("git clone https://github.com/GreyDr34d/O-Pot.git")
        os.system("bash O-Pot/iso/installer/install.sh")

    def service_unistall(self, *args, **kwargs):
        sure = input("Are you sure to uninstall O-pot?[y|n]")
        if sure == "y" or sure == "Y":
            self._delete()

    def service_up(self, *args, **kwargs):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml up -d"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_down(self, *args, **kwargs):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml down"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def _delete(self):
        self.service_down()
        os.system("rm -rf /data /opt/tpot")

    def __str__(self):
        return "opot_module"

    def __add__(self, x):
        return "opot_module" + x
