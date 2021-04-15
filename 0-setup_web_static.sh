#!/usr/bin/env bash
# preparing for deploying

sudo apt-get update -y
sudo apt-get install nginx -y
sudo chown -R "ubuntu":"ubuntu" /etc/nginx/
sudo chown -R "ubuntu":"ubuntu" /var/www/
nginx -s start

sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R "ubuntu":"ubuntu" /data/

echo "this is salah besbes" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# newroot='root \/data\/web_static\/current;'
pattern='root \/var\/www\/html;'
path="/etc/nginx/sites-enabled/default"

newlocation="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"

pattern="root \/var\/www\/html;"
sed -ie "/$pattern/a\ $newlocation" $path

nginx -s reload
