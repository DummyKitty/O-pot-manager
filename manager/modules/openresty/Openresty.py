
import os

class Openresty():
    def __init__(self):

    def service_reload(self):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml exec openresty openresy -s reload "
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)
    def service_stop(self):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml stop openresy"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_start(self,):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml start openresty"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_restart(self):
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml restart openresty"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_proxy_update(self,services,*args,**kwargs):
        