#!/usr/bin/env bash
# preparing for deploying

sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo \
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "$USER":"$USER" /data/
# newroot='root \/data\/web_static\/current;'
pattern='root \/var\/www\/html;'
path="/etc/nginx/sites-enabled/default"

newlocation="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"

pattern="root \/var\/www\/html;"
sed -ie "/$pattern/a\ $newlocation" $path