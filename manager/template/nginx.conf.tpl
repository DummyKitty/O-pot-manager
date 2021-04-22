
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {{
    worker_connections  1024;
}}


http {{
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr $remote_user - [$time_iso8601] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$request_body" "$upstream_addr" "$upstream_http_host" -';
                    #   '"$http_user_agent" "$upstream_http_host" '
                    #   '"$upstream_addr" "$request_body"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

{servers}

}}
