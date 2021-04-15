#!/usr/bin/env bash
# preparing for deploying

sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
sudo chown -R "$USER":"$USER" /data/

echo "Hello AirBnb" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# newroot='root \/data\/web_static\/current;'
pattern='root \/var\/www\/html;'
path="/etc/nginx/sites-enabled/default"

newlocation="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"

pattern="root \/var\/www\/html;"
sed -ie "/$pattern/a\ $newlocation" $path

sudo service nginx start