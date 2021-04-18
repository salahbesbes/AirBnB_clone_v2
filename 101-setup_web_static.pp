# Configures a web server for deployment of web_static.

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root   /var/www/html;
    index  index.html index.htm;
    
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}"
exec { 'update':
  command => 'sudo apt-get update',
  path    => '/usr/bin/:/usr/local/bin/:/bin/';
} ->
package { 'nginx':
  ensure   => present,
  provider => apt;
} ->

file { ['/data',
        '/data/web_static',
        '/data/web_static/releases',
        '/data/web_static/releases/test',
        '/data/web_static/shared']:
  ensure  => directory;
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "Holberton School Puppet\n"
} ->

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test';
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/';
}

file { ['/var/www',
        '/var/www/html']:
  ensure => directory;
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Holberton School Nginx\n';
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $nginx_conf;
} ->

exec { 'nginx restart':
  path => '/etc/init.d/';
}
