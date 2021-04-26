# O-pot-manager
用于O-pot运维的管理程序
安装：
```sh
安装python3、python3-pip
apt update -y
apt install git -y
apt install python3-pip -y

clone项目
git clone https://github.com/GreyDr34d/O-pot-manager.git

安装依赖
python3 -m pip install -r O-pot-manager/manager/requirements.txt
```
使用：sh
```
python3 O-pot-manager/manager/main.py

O-pot manager is a convenient management tool
   ____                    __                  
  / __ \      ____  ____  / /_                
 / / / /_____/ __ \/ __ \/ __/   {1.0 #dev}               
/ /_/ /_____/ /_/ / /_/ / /_                   
\____/     / .___/\____/\__/                
   ____ __/_/____ _____  ____ _____ ____  _____ 
  / __ `__ \/ __ `/ __ \/ __ `/ __ `/ _ \/ ___/ 
 / / / / / / /_/ / / / / /_/ / /_/ /  __/ /    
/_/ /_/ /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                            /____/             
Author:dr34d      Date:2021.04.22
having fun~ 

manager > help
Global commands:
    help                             Print this help menu
    shodan   <service type>          Search for web service domain via shodan
    zoomeye  <service type>          Search for web service domain via zoomeye (Recomand)
    censys   <service type>          Search for web service domain via censys
    fofa     <service type>          Search for web service domain via fofa

    show     <services|cves> <num>   
             services                Show the services
             cves                    Show all latest CVE
    delete   <services|cves>         Delete from knowledge database
    
    use      <modules>               Use modules
             openresty               Use openresty module
             opot                    Use opot module
    banner                           Print banner
    exit                             Exit manager
    
```
使用模块
```sh
manager > use openresty
manager (openresty_module) > help
Global commands:
    help                             Print this help menu
    shodan   <service type>          Search for web service domain via shodan
    zoomeye  <service type>          Search for web service domain via zoomeye (Recomand)
    censys   <service type>          Search for web service domain via censys
    fofa     <service type>          Search for web service domain via fofa

    show     <services|cves> <num>   
             services                Show the services
             cves                    Show all latest CVE
    delete   <services|cves>         Delete from knowledge database
    
    use      <modules>               Use modules
             openresty               Use openresty module
             opot                    Use opot module
    banner                           Print banner
    exit                             Exit manager
    
openresty_module command
    help                                 Print this help menu.
    service  <operation> 
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
                                         services.
    back                                Exit from current module. 
    
manager (openresty_module) > 
```
