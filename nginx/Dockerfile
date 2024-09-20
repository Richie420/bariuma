FROM nginx:alpine

# Install Certbot (Let's Encrypt)
RUN apk add --no-cache certbot certbot-nginx

# Copy the custom NGINX config
COPY nginx.conf /etc/nginx/nginx.conf