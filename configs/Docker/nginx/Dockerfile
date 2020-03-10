FROM nginx:1.17

COPY bin/set_timezone.sh /docker-bin/
COPY nginx/entrypoint_nginx.sh /docker-bin/
COPY nginx/nginx.conf.template /docker-bin/

ARG DPS_NGINX_SERVER_NAME=localhost
ENV DPS_NGINX_SERVER_NAME ${DPS_NGINX_SERVER_NAME}

ENTRYPOINT ["/docker-bin/entrypoint_nginx.sh"]
CMD ["nginx", "-g", "daemon off;"]
