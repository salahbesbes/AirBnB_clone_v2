#!/usr/bin/env bash
# preparing for deploying

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/ 
echo "Salah besbes page" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 

chown ubuntu:ubuntu -R /data/
path="/etc/nginx/sites-available/default"

newlocation="\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"

pattern="root \/var\/www\/html;"

sed -ie "/$pattern/a\ $newlocation" $path
sudo service nginx restart
