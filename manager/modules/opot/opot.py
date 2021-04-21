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
        os.system()

    def __str__(self):
        return "opot_module"

    def __add__(self, x):
        return "opot_module" + x