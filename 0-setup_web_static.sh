#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web static
sudo apt update
sudo apt install nginx -y
sudo /etc/init.d/nginx start
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo -e "Fake text testing nginx config\n" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown ubuntu:ubuntu -R /data
f=/etc/nginx/sites-available/default
sudo rm $f
echo -e "server {
    listen 80 default_server;
    root /usr/share/nginx/html;
    index index.html index.htm;
    add_header X-Served-By $hostname;
    location /redirect_me {
        return 301 https://www.yahoo.com;
    }
    location /hbnb_static {
        alias /data/web_static/current;
    }
}" | sudo tee $f
sudo service nginx restart
