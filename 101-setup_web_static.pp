# Automate the task of preparin environement before deploy
# but with Puppet.

exec { 'update':
  command => 'usr/bin/apt-get update',
}->
package { 'nginx':
  ensure   => installed,
  provider => apt;
}->

file { '/data/webs_tatic':
  ensure => directory;
}->
file { '/data/webs_tatic/releases/test':
  ensure => directory;
}->
file { '/data/webs_tatic/shared':
  ensure => directory;
}->
file { '/data/webs_tatic/releases/test/index.html':
  ensure => present;
  content => "salah server\n"
}->
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}->
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n"
} ->
exec { 'nginx restart':
  path => '/etc/init.d/'
}
