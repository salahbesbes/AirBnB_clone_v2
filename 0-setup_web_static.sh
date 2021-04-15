#!/usr/bin/env bash
# preparing for deploying

sudo apt-get -y update
sudo apt-get install -y nginx
sudo apt-get -y upgrade

sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R "ubuntu":"ubuntu" /data/

echo "this is salah besbes" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# newroot='root \/data\/web_static\/current;'
pattern='root \/var\/www\/html;'
path="/etc/nginx/sites-available/default"

newlocation="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"
sed -ie "/$pattern/a\ $newlocation" $path

sudo service nginx restart
