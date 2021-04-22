#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File        :Openresty.py
@Description :
@Date        :2021/04/22 08:43:46
@Author      :dr34d
@Version     :1.0
'''

import os
from manager.lib.core.db import knowledgeDataBase
from manager.thirdparty.prettytable.prettytable import PrettyTable
from manager.lib.core.data import *


class Openresty():
    server_template = """
    server {{
        listen    {listen_port};
        proxy_set_header Host "{domain}";
        location / {{
            access_log logs/access_8080.log main;
            proxy_pass http://{domain}/;
            proxy_redirect     off;
            proxy_set_header   X-Real-IP        $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
        }}
    }}

    """

    docker_compose_port_template = """
      - "{port}:{port}"
    """

    common_port = ["80", "81", "8080", "8081", "8089", "9000", "10000"]

    weblogic_port = ["7001", "7002"]

    prepare_services = []

    def __init__(self):
        self.knowledgeDb = knowledgeDataBase()

    def service_reload(self, *args, **kwargs):
        """[reload openresty via docker-compose command]
        """
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml exec openresty openresy -s reload "
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_stop(self, *args, **kwargs):
        """[stop openresty via docker-compose command]
        """
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml stop openresy"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_start(self, *args, **kwargs):
        """[start openresty via docker-compose command]
        """
        cmd = "docker-compose -f /opt/tpot/etc/tpot.yaml start openresty"
        try:
            os.system(cmd)
        except Exception as ex:
            print(ex)

    def service_restart(self, *args, **kwargs):
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
        if len(self.prepare_services) > 0:
            reverse_proxies_conf = open(CURRENT_REVERSE_PROXIES_PATH, "w")
            for reverse_proxy in self.prepare_services:
                reverse_proxies_conf.write(
                    " ".join([str(x) for x in reverse_proxy]) + "\n")
            reverse_proxies_conf.close()
            servers = self.gen_servers()

            nginx_conf_template = open(TEMPLATE_DIR + "nginx.conf.tpl").read()
            nginx_conf_content = nginx_conf_template.format(servers=servers)
            os.system(
                "cp /data/openresty/nginx.conf /data/openresty/nginx.conf_bak")
            with open("/data/openresty/nginx.conf", "w") as f:
                f.write(nginx_conf_content)
            f.close()
            self.service_reload()
        else:
            print("please add services")
            self.service_list()

    def service_add(self, *args, **kwargs):
        """[summary]

        Args:
            service_type ([type]): [description]
            number ([type]): [description]
        """
        ids = args[0].strip().split()

        if len(ids):
            for i in ids:
                res = self.knowledgeDb.select("services", id=i)
                if res:
                    self.prepare_services.append(res)
        elif number:
            self.prepare_services.extend(
                self.knowledgeDb.select("services",
                                        service_name=service_type,
                                        limit=number))
        else:
            self.prepare_services.extend(
                self.knowledgeDb.select("services",
                                        service_name=service_type,
                                        limit=5))
        self.service_list()

    def service_list(self, *args, **kwargs):
        tb = PrettyTable(["id", "service_type", "domain", "ip", "port"])
        for i in self.prepare_services:
            tb.add_row(i)
        print(tb)

    def service_clear(self, *args, **kwargs):
        self.prepare_services = []
        self.service_list()

    def service_current(self):
        print("Current selections:")
        tb = PrettyTable(["id", "service_type", "domain", "ip", "port"])
        print(tb)

    def gen_servers(self):
        servers = ""
        for i in range(len(self.prepare_services)):
            if i < len(self.common_port):
                domain = self.prepare_services[i][2]
                port = self.common_port[i]
                servers += self.server_template.format(listen_port=port,
                                                       domain=domain)

        return servers

    def __str__(self):
        return "openresty_module"

    def __add__(self, x):
        return "openresty_module" + x


if __name__ == "__main__":
    c = Openresty()
    print("aaaa{}aa".format(c))
    print(c + "aaaa")
