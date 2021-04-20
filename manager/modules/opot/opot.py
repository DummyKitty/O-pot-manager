

import os

class Opot():
    def __init__(self):

    def service_stop(self):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml stop"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_start(self,):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml start"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_restart(self):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml restart"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_status(self):
        try:
            os.system("bash /opt/tpot/bin/dps.sh")
        except:
            return
    def service_install(self):
        os.system()