import os


class Openresty():
    def service_reload(self):
        """[reload openresty via docker-compose command]
        """
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml exec openresty openresy -s reload "
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_stop(self):
        """[stop openresty via docker-compose command]
        """
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml stop openresy"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_start(self, ):
        """[start openresty via docker-compose command]
        """
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml start openresty"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_restart(self):
        """[restart openresty via docker-compose command]
        """
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml restart openresty"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_update(self, services, *args, **kwargs):
        """[update the proxy setting]

        Args:
            services (["service_type","domain","ip","port"]): [content from the knowleageDb]
        """

    def __str__(self):
        return "openresty_module"


if __name__ == "__main__":
    c = Openresty()
    print("aaaa{}aa".format(c))