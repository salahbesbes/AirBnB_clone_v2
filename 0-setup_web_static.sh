#!/usr/bin/env bash
# Bash Script to Setup Airbnb Static_web 
sudo apt-get update -y
sudo apt-get updgrade -y
sudo apt-get install -y nginx
mkdir -p  /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir /data/web_static/shared/
echo "Hello AirBnb" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 
chown ubuntu:ubuntu -hR /data/

path='\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n'
pattern='root \/var\/www\/html;'
sudo sed "/$pattern/ a \ $newlocation" $path
sudo service nginx restart
