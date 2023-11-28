# Install nginx with puppet
package { 'nginx':
  ensure   => '1.18.0',
  provider => 'apt',
}

file { 'Hello World':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World',
}

file_line { 'Hello World':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => '\trewrite ^/redirect_me https://youtu.be/xCPy1jvOp90?si=FOI5kpF1izE9npTi permanent;',
}

exec { 'service':
  command  => 'service nginx start',
  provider => 'shell',
  user     => 'root',
  path     => '/usr/sbin/service',
}