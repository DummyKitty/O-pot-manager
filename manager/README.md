# tools-console

用于管理反向代理、查看数据、导出数据等

功能：
- openresty模块
  - 反向代理配置映射的查询
  - 修改反向代理映射
- 插件
  - zoomeye
  - censys
  - 
- 前端
  - 一个console界面
  - linux shell命令支持
  - banner
- 数据库
  - sqlite

```sh
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
    
opot_module command
    help                                Print this help menu.
    service <operation> 
            stop                        Stop opot.
            start                       Start opot.
            restart                     Restart opot.
            status                      Show the opot status.
            up                          Up the opot in daemon.
            down                        Down the opot.
            install                     Install the opot.
            unistall                    Unistall the opot.
    back                                Exit from current module. 
    
 ```
