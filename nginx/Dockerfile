FROM nginx:1.29.6-alpine3.23

COPY nginx.conf /etc/nginx/nginx.conf

RUN rm /etc/nginx/conf.d/default.conf && \
	chmod 444 /etc/nginx/nginx.conf

EXPOSE 80
