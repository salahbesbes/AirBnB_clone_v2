#!/usr/bin/env bash
# preparing for deploying
sudo mkdir -p /data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "$USER":"$USER" /data/
newroot="/data/web_static/current"

sudo sed  "s/root \/var\/www\/html;/ $newroot/g" /etc/nginx/sites-available/default