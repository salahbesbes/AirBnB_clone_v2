#!/usr/bin/env bash
# preparing for deploying

sudo apt-get update
sudo apt-get install nginx

sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R "$USER":"$USER" /data/

echo "Hello AirBnb" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# newroot='root \/data\/web_static\/current;'
pattern='root \/var\/www\/html;'
path="/etc/nginx/sites-enabled/default"

newlocation="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"

pattern="root \/var\/www\/html;"
sed -ie "/$pattern/a\ $newlocation" $path

sudo service nginx restart