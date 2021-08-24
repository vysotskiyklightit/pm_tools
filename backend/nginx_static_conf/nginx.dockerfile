# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15

COPY /nginx_static_conf/nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /app/
COPY ./static/ ./media/ ./
