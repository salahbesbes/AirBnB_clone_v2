# Automate the task of preparin environement before deploy
# but with Puppet.

exec { 'update':
  command => 'usr/bin/apt-get apdate',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'];
}

exec { 'folder creation':
  command => '/bin/mkdir -p  /data/web_static/;
        /bin/mkdir -p /data/web_static/releases/test/;
        /bin/mkdir /data/web_static/shared/',
}
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'this is salah server';
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode => '0644'
  require => Package['nginx']
}

exec { 'create linkedFile':
  command => '/usr/bin/ln -sf /data/web_static/releases/test /data/web_static/current',
}

file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  recurse => true,
  group   => 'ubuntu',
  mode    => '0644';
}

file_line { '/etc/nginx/sites-available/default':
  ensure  => present,
  after   => 'listen \[::\]:80',
  line    => "add_header X-Served-By ${hostname};",
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx'];
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
