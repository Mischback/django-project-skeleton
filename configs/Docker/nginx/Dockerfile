FROM nginx:1.17

COPY bin/set_timezone.sh /docker-bin/
COPY nginx/entrypoint_nginx.sh /docker-bin/
COPY nginx/nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["/docker-bin/entrypoint_nginx.sh"]
CMD ["nginx", "-g", "daemon off;"]
